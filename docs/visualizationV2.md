# Visualization V2

## Overview

The visualization module provides functions to create various visual representations of the risk assessment results. These visualizations help in understanding the complex relationships between risks, their impacts under different scenarios, and other key insights from the analysis.

## Key Functions

### `generate_visualizations(risks: List[Risk], risk_interactions: List[RiskInteraction], simulation_results: Dict[str, Dict[int, SimulationResult]], sensitivity_results: Dict[str, Dict[str, float]], time_series_results: Dict[int, List[float]])`

This function generates a comprehensive set of visualizations based on the risk assessment results.

#### Input
- `risks`: A list of `Risk` objects.
- `risk_interactions`: A list of `RiskInteraction` objects.
- `simulation_results`: Results from Monte Carlo simulations.
- `sensitivity_results`: Results from sensitivity analysis.
- `time_series_results`: Results from time series analysis.

#### Output
- This function saves various visualization files (PNG format) in the specified output directory.

### `risk_matrix(risks: List[Risk])`

This function creates a risk matrix visualization, plotting risks based on their likelihood and impact.

#### Input
- `risks`: A list of `Risk` objects.

#### Output
- Saves a 'risk_matrix.png' file in the output directory.

### `interaction_heatmap(risks: List[Risk], risk_interactions: List[RiskInteraction])`

This function creates a heatmap visualization of risk interactions.

#### Input
- `risks`: A list of `Risk` objects.
- `risk_interactions`: A list of `RiskInteraction` objects.

#### Output
- Saves an 'interaction_heatmap.png' file in the output directory.

### `interaction_network(risks: List[Risk], risk_interactions: List[RiskInteraction])`

This function creates a network graph visualization of risk interactions.

#### Input
- `risks`: A list of `Risk` objects.
- `risk_interactions`: A list of `RiskInteraction` objects.

#### Output
- Saves an 'interaction_network.png' file in the output directory.

### `monte_carlo_results(simulation_results: Dict[str, Dict[int, SimulationResult]])`

This function visualizes the results of Monte Carlo simulations.

#### Input
- `simulation_results`: A dictionary containing simulation results for each scenario and risk.

#### Output
- Saves a 'monte_carlo_results.png' file in the output directory.

### `sensitivity_analysis_heatmap(sensitivity_results: Dict[str, Dict[str, float]])`

This function creates a heatmap visualization of sensitivity analysis results.

#### Input
- `sensitivity_results`: A dictionary containing sensitivity analysis results.

#### Output
- Saves a 'sensitivity_analysis_heatmap.png' file in the output directory.

### `time_series_projection(risks: List[Risk], time_series_results: Dict[int, List[float]])`

This function visualizes the projected time series of risk impacts.

#### Input
- `risks`: A list of `Risk` objects.
- `time_series_results`: A dictionary containing time series projections for each risk.

#### Output
- Saves a 'time_series_projection.png' file in the output directory.

## Usage Notes

- All visualizations are saved as PNG files in the directory specified by the `OUTPUT_DIR` configuration variable.
- The visualizations use a consistent color scheme and styling for coherence across different plots.
- Some visualizations (like the interaction network) may become cluttered with a large number of risks. In such cases, consider filtering to show only the most significant interactions or risks.
- The `matplotlib` and `seaborn` libraries are used for creating these visualizations. Ensure these libraries are properly installed and configured in your environment.

These visualizations provide powerful tools for communicating complex risk assessment results to stakeholders, allowing for quick identification of key risks, their interactions, and their behavior under different scenarios.