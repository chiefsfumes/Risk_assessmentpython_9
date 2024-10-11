import pytest
import networkx as nx
from src.risk_analysis.systemic_risk_analysis import (
    analyze_systemic_risks, identify_trigger_points, assess_resilience,
    is_systemic_risk, identify_systemic_factor, identify_relevant_external_factors,
    calculate_scenario_resilience, assess_system_resilience
)
from src.models import Risk, ExternalData, SimulationResult

# Keep existing fixtures and tests

def test_assess_system_resilience(sample_risks, sample_risk_network):
    scenario_impacts = {
        "Scenario1": [(risk, 0.8) for risk in sample_risks],
        "Scenario2": [(risk, 0.6) for risk in sample_risks],
    }
    
    resilience_metrics = assess_system_resilience(sample_risks, sample_risk_network, scenario_impacts)
    
    assert isinstance(resilience_metrics, dict)
    assert "network_density" in resilience_metrics
    assert "average_clustering" in resilience_metrics
    assert "assortativity" in resilience_metrics
    assert "Scenario1_impact_dispersion" in resilience_metrics
    assert "Scenario2_impact_dispersion" in resilience_metrics
    assert "adaptive_capacity" in resilience_metrics
    
    assert all(0 <= value <= 1 for value in resilience_metrics.values())

# Keep existing code below this line