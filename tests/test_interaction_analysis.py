import pytest
import networkx as nx
import numpy as np
from src.risk_analysis.interaction_analysis import (
    analyze_risk_interactions, build_risk_network, identify_central_risks,
    detect_risk_clusters, analyze_risk_cascades, calculate_risk_correlations,
    identify_risk_feedback_loops, analyze_network_resilience, generate_risk_interaction_summary,
    create_risk_interaction_matrix, simulate_risk_interactions
)
from src.models import Risk, RiskInteraction

# Keep existing fixtures and tests

def test_create_risk_interaction_matrix(sample_risks):
    interaction_matrix = create_risk_interaction_matrix(sample_risks)
    
    assert isinstance(interaction_matrix, np.ndarray)
    assert interaction_matrix.shape == (len(sample_risks), len(sample_risks))
    assert np.all(interaction_matrix >= 0) and np.all(interaction_matrix <= 1)
    assert np.allclose(interaction_matrix, interaction_matrix.T)  # Check symmetry

def test_simulate_risk_interactions(sample_risks):
    interaction_matrix = np.random.rand(len(sample_risks), len(sample_risks))
    np.fill_diagonal(interaction_matrix, 0)
    
    risk_progression = simulate_risk_interactions(sample_risks, interaction_matrix)
    
    assert isinstance(risk_progression, dict)
    assert len(risk_progression) == len(sample_risks)
    for risk_id, progression in risk_progression.items():
        assert len(progression) == 11  # Initial state + 10 time steps
        assert all(0 <= value <= 1 for value in progression)

# Keep existing code below this line