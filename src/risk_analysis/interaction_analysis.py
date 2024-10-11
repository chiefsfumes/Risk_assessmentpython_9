from typing import List, Dict, Tuple
from src.models import Risk, RiskInteraction
from src.config import LLM_MODEL, LLM_API_KEY
from src.prompts import INTERACTION_ANALYSIS_PROMPT
import openai
import networkx as nx
import numpy as np
from scipy.stats import pearsonr
from sklearn.cluster import KMeans

openai.api_key = LLM_API_KEY

# Keep existing functions

def create_risk_interaction_matrix(risks: List[Risk]) -> np.ndarray:
    n = len(risks)
    matrix = np.zeros((n, n))
    for i, risk1 in enumerate(risks):
        for j, risk2 in enumerate(risks[i+1:], start=i+1):
            interaction = analyze_single_interaction(risk1, risk2)
            matrix[i, j] = matrix[j, i] = interaction.interaction_score
    return matrix

def analyze_single_interaction(risk1: Risk, risk2: Risk) -> RiskInteraction:
    prompt = INTERACTION_ANALYSIS_PROMPT.format(
        risk1_description=risk1.description,
        risk1_category=risk1.category,
        risk1_subcategory=risk1.subcategory,
        risk2_description=risk2.description,
        risk2_category=risk2.category,
        risk2_subcategory=risk2.subcategory
    )

    response = openai.ChatCompletion.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": "You are an expert in climate risk assessment and risk interactions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=400
    )

    analysis = response.choices[0].message['content']
    interaction_score = extract_interaction_score(analysis)
    interaction_type = determine_interaction_type(interaction_score)
    return RiskInteraction(risk1.id, risk2.id, interaction_score, interaction_type)

def simulate_risk_interactions(risks: List[Risk], interaction_matrix: np.ndarray, num_steps: int = 10) -> Dict[int, List[float]]:
    n = len(risks)
    risk_levels = np.array([risk.impact for risk in risks])
    risk_progression = {risk.id: [risk.impact] for risk in risks}

    for _ in range(num_steps):
        influence = interaction_matrix @ risk_levels
        risk_levels = np.clip(risk_levels + 0.1 * influence, 0, 1)
        for i, risk in enumerate(risks):
            risk_progression[risk.id].append(risk_levels[i])

    return risk_progression

# Keep existing code below this line