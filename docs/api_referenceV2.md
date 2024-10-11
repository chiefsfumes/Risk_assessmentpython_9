# API Reference V2

## Overview
This document provides a detailed reference for the key classes and functions in the Climate Risk Assessment Tool.

## Classes

### Risk
Represents a climate-related risk.

Attributes:
- `id` (int): Unique identifier for the risk
- `description` (str): Description of the risk
- `category` (str): Category of the risk (e.g., "Physical", "Transition")
- `subcategory` (str): Subcategory of the risk
- `tertiary_category` (str): Tertiary category of the risk
- `likelihood` (float): Current likelihood of the risk (0-1)
- `impact` (float): Current impact of the risk (0-1)
- `time_horizon` (str): Time horizon of the risk
- `industry_specific` (bool): Whether the risk is industry-specific
- `sasb_category` (str): SASB category of the risk

### Scenario
Represents a climate scenario.

Attributes:
- `name` (str): Name of the scenario
- `temp_increase` (float): Temperature increase in °C
- `carbon_price` (float): Carbon price in $/ton
- `renewable_energy` (float): Renewable energy share (0-1)
- `policy_stringency` (float): Policy stringency (0-1)
- `biodiversity_loss` (float): Biodiversity loss (0-1)
- `ecosystem_degradation` (float): Ecosystem degradation (0-1)
- `financial_stability` (float): Financial stability (0-1)
- `supply_chain_disruption` (float): Supply chain disruption (0-1)

## Functions

### Data Loading

`load_risk_data(file_path: str) -> List[Risk]`
Loads risk data from a CSV file.

`load_external_data(file_path: str) -> Dict[str, ExternalData]`
Loads external data from a CSV file.

### Risk Analysis

`categorize_risks(risks: List[Risk]) -> Dict[str, List[Risk]]`
Categorizes risks based on their primary category.

`categorize_risks_multi_level(risks: List[Risk]) -> Dict[str, Dict[str, List[Risk]]]`
Categorizes risks based on their primary and secondary categories.

`prioritize_risks(risks: List[Risk]) -> Dict[str, List[Risk]]`
Prioritizes risks based on their impact and likelihood.

`conduct_advanced_risk_analysis(risks: List[Risk], scenarios: Dict[str, Scenario], company_industry: str, key_dependencies: List[str], external_data: Dict) -> Dict`
Performs comprehensive risk analysis including LLM-based assessments, interaction analysis, and more.

### Scenario Analysis

`simulate_scenario_impact(risks: List[Risk], external_data: Dict[str, ExternalData], scenario: Scenario) -> List[Tuple[Risk, float]]`
Simulates the impact of a given scenario on the provided risks.

`monte_carlo_simulation(risks: List[Risk], external_data: Dict[str, ExternalData], scenarios: Dict[str, Scenario]) -> Dict[str, Dict[int, SimulationResult]]`
Performs Monte Carlo simulations for each risk under different scenarios.

### Interaction Analysis

`analyze_risk_interactions(risks: List[Risk]) -> List[RiskInteraction]`
Analyzes interactions between risks using LLM.

`build_risk_network(risks: List[Risk], interactions: List[RiskInteraction]) -> nx.Graph`
Builds a network graph of risk interactions.

`identify_central_risks(G: nx.Graph) -> Dict[int, float]`
Identifies central risks in the risk network.

### Reporting

`generate_report(risks: List[Risk], ...) -> str`
Generates a comprehensive report in JSON format and creates an HTML version.

### Visualization

`generate_visualizations(risks: List[Risk], ...)`
Generates a set of visualizations based on the risk assessment results.

## Usage Examples

```python
# Load data
risks = load_risk_data('data/risk_data.csv')
external_data = load_external_data('data/external_data.csv')

# Perform analysis
categorized_risks = categorize_risks(risks)
advanced_analysis = conduct_advanced_risk_analysis(risks, SCENARIOS, "Energy", ["Oil suppliers", "Renewable energy"], external_data)

# Generate report
report = generate_report(risks, advanced_analysis, ...)

# Create visualizations
generate_visualizations(risks, advanced_analysis, ...)
```

For more detailed information on each function and class, refer to the inline documentation in the source code.