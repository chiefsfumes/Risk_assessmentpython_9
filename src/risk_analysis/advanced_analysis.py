from typing import List, Dict, Any
from src.models import Risk, Scenario, PESTELAnalysis, SystemicRisk
from src.config import LLM_MODEL, LLM_API_KEY, SCENARIOS
from src.prompts import (RISK_NARRATIVE_PROMPT, EXECUTIVE_INSIGHTS_PROMPT, 
                         SYSTEMIC_RISK_PROMPT, MITIGATION_STRATEGY_PROMPT, 
                         PESTEL_ANALYSIS_PROMPT)
import openai
import numpy as np
import re
from src.risk_analysis.pestel_analysis import perform_pestel_analysis
from src.risk_analysis.sasb_integration import integrate_sasb_materiality
from src.risk_analysis.systemic_risk_analysis import analyze_systemic_risks, identify_trigger_points, assess_resilience
from src.risk_analysis.interaction_analysis import analyze_risk_interactions, build_risk_network, create_risk_interaction_matrix, simulate_risk_interactions

openai.api_key = LLM_API_KEY

# Keep existing functions

def assess_aggregate_impact(risks: List[Risk], interaction_matrix: np.ndarray, num_simulations: int = 1000) -> Dict[str, float]:
    n = len(risks)
    base_impacts = np.array([risk.impact for risk in risks])
    
    aggregate_impacts = []
    for _ in range(num_simulations):
        risk_levels = np.random.beta(2, 2, n) * base_impacts
        for _ in range(10):  # Simulate interactions for 10 time steps
            influence = interaction_matrix @ risk_levels
            risk_levels = np.clip(risk_levels + 0.1 * influence, 0, 1)
        aggregate_impacts.append(np.sum(risk_levels))
    
    return {
        "mean": np.mean(aggregate_impacts),
        "median": np.median(aggregate_impacts),
        "95th_percentile": np.percentile(aggregate_impacts, 95),
        "max": np.max(aggregate_impacts)
    }

def identify_tipping_points(risks: List[Risk], interaction_matrix: np.ndarray) -> List[Dict[str, Any]]:
    n = len(risks)
    base_impacts = np.array([risk.impact for risk in risks])
    tipping_points = []

    for i in range(n):
        impact_levels = np.linspace(0, 1, 100)
        aggregate_impacts = []
        for level in impact_levels:
            risk_levels = base_impacts.copy()
            risk_levels[i] = level
            for _ in range(10):  # Simulate interactions for 10 time steps
                influence = interaction_matrix @ risk_levels
                risk_levels = np.clip(risk_levels + 0.1 * influence, 0, 1)
            aggregate_impacts.append(np.sum(risk_levels))
        
        # Detect sudden changes in the rate of change
        rate_of_change = np.diff(aggregate_impacts)
        threshold = np.mean(rate_of_change) + 2 * np.std(rate_of_change)
        tipping_point_indices = np.where(rate_of_change > threshold)[0]
        
        if len(tipping_point_indices) > 0:
            tipping_points.append({
                "risk_id": risks[i].id,
                "risk_description": risks[i].description,
                "tipping_point_level": impact_levels[tipping_point_indices[0]],
                "aggregate_impact": aggregate_impacts[tipping_point_indices[0]]
            })
    
    return tipping_points

# Keep existing code below this line