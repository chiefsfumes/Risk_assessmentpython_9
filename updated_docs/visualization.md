# Visualization

## Overview

The visualization module provides functions to create various visual representations of the risk assessment results. These visualizations help in understanding the complex relationships between risks, their impacts under different scenarios, and other key insights from the analysis.

## Key Functions

### `generate_visualizations(risks: List[Risk], risk_interactions: List[RiskInteraction], simulation_results: Dict[str, Dict[int, SimulationResult]], sensitivity_results: Dict[str, Dict[str, float]], time_series_results: Dict[int, List[float]], risk_network: nx.Graph, risk_clusters: Dict[int, int], cumulative_impact: List[float], interaction_matrix: np.ndarray, risk_progression: Dict[int, List[float]], aggregate_impact: Dict[str, float])`

This function generates a comprehensive set of visualizations based on the risk assessment results.

### `risk_matrix(risks: List[Risk])`

Creates a risk matrix visualization, plotting risks based on their likelihood and impact.

### `interaction_heatmap(risks: List[Risk], risk_interactions: List[RiskInteraction])`

Creates a heatmap visualization of risk interactions.

### `interaction_network(risks: List[Risk], risk_interactions: List[RiskInteraction], risk_network: nx.Graph, risk_clusters: Dict[int, int])`

Creates a network graph visualization of risk interactions, including clustering information.

### `monte_carlo_results(simulation_results: Dict[str, Dict[int, SimulationResult]])`

Visualizes the results of Monte Carlo simulations.

### `sensitivity_analysis_heatmap(sensitivity_results: Dict[str, Dict[str, float]])`

Creates a heatmap visualization of sensitivity analysis results.

### `time_series_projection(risks: List[Risk], time_series_results: Dict[int, List[float]])`

Visualizes the projected time series of risk impacts.

### `cumulative_impact_plot(cumulative_impact: List[float])`

Plots the forecasted cumulative impact of all risks over time.

### `interaction_matrix_heatmap(risks: List[Risk], interaction_matrix: np.ndarray)`

Creates a heatmap visualization of the risk interaction matrix.

### `risk_progression_plot(risks: List[Risk], risk_progression: Dict[int, List[float]])`

Visualizes the simulated progression of risk levels over time.

### `aggregate_impact_distribution(aggregate_impact: Dict[str, float])`

Plots the distribution of aggregate impact values.

## Usage Example

```python
generate_visualizations(
    risks,
    risk_interactions,
    simulation_results,
    sensitivity_results,
    time_series_results,
    risk_network,
    risk_clusters,
    cumulative_impact,
    interaction_matrix,
    risk_progression,
    aggregate_impact
)
```

## Key Considerations

- All visualizations are saved as PNG files in the directory specified by the `OUTPUT_DIR` configuration variable.
- The visualizations use a consistent color scheme and styling for coherence across different plots.
- Some visualizations (like the interaction network) may become cluttered with a large number of risks. In such cases, consider filtering to show only the most significant interactions or risks.
- The `matplotlib` and `seaborn` libraries are used for creating these visualizations. Ensure these libraries are properly installed and configured in your environment.

## Customization

You can customize the visualizations by modifying the following in `src/config.py`:

- `VIZ_DPI`: Set the resolution (dots per inch) for saved visualizations
- `HEATMAP_CMAP`: Specify the color map used for heatmap visualizations

## Integration with Other Modules

The visualization module integrates closely with other modules:

- It uses outputs from the risk analysis, scenario analysis, interaction analysis, and time series analysis modules.
- The generated visualizations are referenced in the HTML report created by the reporting module.

For more detailed information on the implementation of each function, refer to the source code and inline documentation in `src/visualization.py`.