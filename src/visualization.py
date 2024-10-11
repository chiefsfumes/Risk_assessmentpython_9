import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict
import pandas as pd
import numpy as np
import networkx as nx
import os
from src.models import Risk, RiskInteraction, SimulationResult
from src.config import OUTPUT_DIR, VIZ_DPI, HEATMAP_CMAP, TIME_SERIES_HORIZON

def generate_visualizations(risks: List[Risk], risk_interactions: List[RiskInteraction], 
                            simulation_results: Dict[str, Dict[int, SimulationResult]],
                            sensitivity_results: Dict[str, Dict[str, float]],
                            time_series_results: Dict[int, List[float]],
                            risk_network: nx.Graph,
                            risk_clusters: Dict[int, int],
                            cumulative_impact: List[float],
                            interaction_matrix: np.ndarray,
                            risk_progression: Dict[int, List[float]],
                            aggregate_impact: Dict[str, float]):
    risk_matrix(risks)
    interaction_heatmap(risks, risk_interactions)
    interaction_network(risks, risk_interactions, risk_network, risk_clusters)
    monte_carlo_results(simulation_results)
    sensitivity_analysis_heatmap(sensitivity_results)
    time_series_projection(risks, time_series_results)
    cumulative_impact_plot(cumulative_impact)
    interaction_matrix_heatmap(risks, interaction_matrix)
    risk_progression_plot(risks, risk_progression)
    aggregate_impact_distribution(aggregate_impact)

# Keep existing functions

def interaction_matrix_heatmap(risks: List[Risk], interaction_matrix: np.ndarray):
    plt.figure(figsize=(12, 10))
    sns.heatmap(interaction_matrix, annot=True, cmap=HEATMAP_CMAP, xticklabels=[r.id for r in risks], yticklabels=[r.id for r in risks])
    plt.title('Risk Interaction Matrix')
    plt.savefig(os.path.join(OUTPUT_DIR, 'interaction_matrix_heatmap.png'), dpi=VIZ_DPI)
    plt.close()

def risk_progression_plot(risks: List[Risk], risk_progression: Dict[int, List[float]]):
    plt.figure(figsize=(12, 8))
    for risk_id, progression in risk_progression.items():
        plt.plot(progression, label=f'Risk {risk_id}')
    plt.xlabel('Time Steps')
    plt.ylabel('Risk Level')
    plt.title('Risk Progression Over Time')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'risk_progression.png'), dpi=VIZ_DPI)
    plt.close()

def aggregate_impact_distribution(aggregate_impact: Dict[str, float]):
    plt.figure(figsize=(10, 6))
    impact_values = list(aggregate_impact.values())
    sns.histplot(impact_values, kde=True)
    plt.axvline(aggregate_impact['mean'], color='r', linestyle='--', label='Mean')
    plt.axvline(aggregate_impact['95th_percentile'], color='g', linestyle='--', label='95th Percentile')
    plt.xlabel('Aggregate Impact')
    plt.ylabel('Frequency')
    plt.title('Distribution of Aggregate Impact')
    plt.legend()
    plt.savefig(os.path.join(OUTPUT_DIR, 'aggregate_impact_distribution.png'), dpi=VIZ_DPI)
    plt.close()

# Keep existing code below this line