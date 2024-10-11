import pytest
import numpy as np
from src.risk_analysis.advanced_analysis import (
    conduct_advanced_risk_analysis, generate_risk_narratives,
    generate_executive_insights, perform_cross_scenario_analysis,
    identify_key_uncertainties, generate_mitigation_strategies,
    assess_aggregate_impact, identify_tipping_points
)
from src.models import Risk, Scenario

# Keep existing fixtures and tests

def test_assess_aggregate_impact(sample_risks):
    interaction_matrix = np.random.rand(len(sample_risks), len(sample_risks))
    np.fill_diagonal(interaction_matrix, 0)
    
    aggregate_impact = assess_aggregate_impact(sample_risks, interaction_matrix)
    
    assert isinstance(aggregate_impact, dict)
    assert "mean" in aggregate_impact
    assert "median" in aggregate_impact
    assert "95th_percentile" in aggregate_impact
    assert "max" in aggregate_impact
    assert all(0 <= value <= len(sample_risks) for value in aggregate_impact.values())

def test_identify_tipping_points(sample_risks):
    interaction_matrix = np.random.rand(len(sample_risks), len(sample_risks))
    np.fill_diagonal(interaction_matrix, 0)
    
    tipping_points = identify_tipping_points(sample_risks, interaction_matrix)
    
    assert isinstance(tipping_points, list)
    for tp in tipping_points:
        assert "risk_id" in tp
        assert "risk_description" in tp
        assert "tipping_point_level" in tp
        assert "aggregate_impact" in tp
        assert 0 <= tp["tipping_point_level"] <= 1
        assert tp["aggregate_impact"] > 0

# Keep existing code below this line