# Interaction Analysis

## Overview

The interaction analysis module examines the relationships and interdependencies between different climate risks. It uses network analysis techniques and language models to identify and quantify risk interactions, central risks, and potential cascading effects.

## Key Functions

### `analyze_risk_interactions(risks: List[Risk]) -> List[RiskInteraction]`

Analyzes potential interactions between pairs of risks using language models.

### `build_risk_network(risks: List[Risk], interactions: List[RiskInteraction]) -> nx.Graph`

Constructs a network graph representing risk interactions.

### `identify_central_risks(G: nx.Graph) -> Dict[int, float]`

Identifies central risks in the risk network using various centrality measures.

### `detect_risk_clusters(G: nx.Graph) -> Dict[int, int]`

Detects clusters of closely related risks in the network.

### `analyze_risk_cascades(G: nx.Graph, initial_risks: List[int]) -> Dict[int, List[int]]`

Analyzes potential cascading effects starting from specified initial risks.

### `create_risk_interaction_matrix(risks: List[Risk]) -> np.ndarray`

Creates a matrix representation of risk interactions.

### `simulate_risk_interactions(risks: List[Risk], interaction_matrix: np.ndarray, num_steps: int = 10) -> Dict[int, List[float]]`

Simulates the progression of risk levels over time based on their interactions.

## Usage Example

```python
# Load risks
risks = load_risk_data('data/risk_data.csv')

# Analyze risk interactions
risk_interactions = analyze_risk_interactions(risks)

# Build risk network
risk_network = build_risk_network(risks, risk_interactions)

# Identify central risks
central_risks = identify_central_risks(risk_network)

# Detect risk clusters
risk_clusters = detect_risk_clusters(risk_network)

# Analyze risk cascades
initial_risks = [r.id for r in risks if r.impact > 0.8]
risk_cascades = analyze_risk_cascades(risk_network, initial_risks)

# Create interaction matrix
interaction_matrix = create_risk_interaction_matrix(risks)

# Simulate risk interactions
risk_progression = simulate_risk_interactions(risks, interaction_matrix)
```

## Key Considerations

- The module uses language models to provide sophisticated analysis of risk interactions.
- Network analysis techniques help identify central risks and clusters.
- The risk cascade analysis helps understand potential domino effects in the risk landscape.
- The interaction matrix and simulation provide a quantitative view of how risks influence each other over time.

## Customization

You can customize the interaction analysis by modifying the following in `src/config.py`:

- `LLM_MODEL`: Specify the language model used for interaction analysis
- `NUM_CLUSTERS`: Set the number of clusters for risk clustering

For more detailed information on the implementation of each function, refer to the source code and inline documentation in `src/risk_analysis/interaction_analysis.py`.

## Visualization

The results of the interaction analysis can be visualized using functions in the visualization module:

- `interaction_heatmap`: Visualizes the interaction matrix
- `interaction_network`: Creates a network graph visualization of risk interactions

These visualizations help in understanding the complex relationships between different risks and identifying key patterns in the risk landscape.