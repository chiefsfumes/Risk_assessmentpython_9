from typing import List, Dict
from src.models import Risk

def categorize_risks(risks: List[Risk]) -> Dict[str, List[Risk]]:
    categories = {}
    for risk in risks:
        if risk.category not in categories:
            categories[risk.category] = []
        categories[risk.category].append(risk)
    return categories

def categorize_risks_multi_level(risks: List[Risk]) -> Dict[str, Dict[str, List[Risk]]]:
    categories = {}
    for risk in risks:
        if risk.category not in categories:
            categories[risk.category] = {}
        if risk.subcategory not in categories[risk.category]:
            categories[risk.category][risk.subcategory] = []
        categories[risk.category][risk.subcategory].append(risk)
    return categories

def assign_risk_priority(risk: Risk) -> str:
    if risk.impact > 0.7 and risk.likelihood > 0.7:
        return "High"
    elif risk.impact > 0.3 and risk.likelihood > 0.3:
        return "Medium"
    else:
        return "Low"

def prioritize_risks(risks: List[Risk]) -> Dict[str, List[Risk]]:
    priorities = {"High": [], "Medium": [], "Low": []}
    for risk in risks:
        priority = assign_risk_priority(risk)
        priorities[priority].append(risk)
    return priorities

def integrate_sasb_materiality(risks: List[Risk], industry: str) -> Dict[str, List[Risk]]:
    # This is a placeholder function. The actual implementation should be in src/risk_analysis/sasb_integration.py
    from src.risk_analysis.sasb_integration import integrate_sasb_materiality as sasb_integration
    return sasb_integration(risks, industry)

def perform_pestel_analysis(risks: List[Risk], external_data: Dict[str, 'ExternalData']) -> Dict[str, List[Dict[str, str]]]:
    # This is a placeholder function. The actual implementation should be in src/risk_analysis/pestel_analysis.py
    from src.risk_analysis.pestel_analysis import perform_pestel_analysis as pestel_analysis
    return pestel_analysis(risks, external_data)