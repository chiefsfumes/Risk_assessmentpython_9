# API Reference

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
- `biodiversity_index` (float): Biodiversity index (0-1)
- `ecosystem_health` (float): Ecosystem health (0-1)
- `financial_system_stability` (float): Financial system stability (0-1)
- `global_supply_chain_resilience` (float): Global supply chain resilience (0-1)

### ExternalData
Represents external data for a given year.

Attributes:
- `year` (int): The year of the data
- `gdp_growth` (float): GDP growth rate
- `population` (int): Population
- `energy_demand` (float): Energy demand
- `carbon_price` (float): Carbon price
- `renewable_energy_share` (float): Renewable energy share
- `biodiversity_index` (float): Biodiversity index
- `deforestation_rate` (float): Deforestation rate

### RiskInteraction
Represents an interaction between two risks.

Attributes:
- `risk1_id` (int): ID of the first risk
- `risk2_id` (int): ID of the second risk
- `interaction_score` (float): Strength of the interaction (0-1)
- `interaction_type` (str): Type of interaction (e.g., "Strong", "Moderate", "Weak")

### SimulationResult
Represents the result of a Monte Carlo simulation for a risk under a specific scenario.

Attributes:
- `risk_id` (int): ID of the risk
- `scenario` (str): Name of the scenario
- `impact_distribution` (List[float]): Distribution of simulated impacts
- `likelihood_distribution` (List[float]): Distribution of simulated likelihoods

## Functions

### Data Loading

`load_risk_data(file_path: str) -> List[Risk]`
Loads risk data from a CSV file.

`load_external_data(file_path: str) -> Dict[str, ExternalData]`
Loads external data from a CSV file.

`extract_risk_statements_from_10k(file_path: str) -> List[Dict[str, str]]`
Extracts risk statements from a 10-K filing using NLP techniques.

### Risk Analysis

`categorize_risks(risks: List[Risk]) -> Dict[str, List[Risk]]`
Categorizes risks based on their primary category.

`categorize_risks_multi_level(risks: List[Risk]) -> Dict[str, Dict[str, List[Risk]]]`
Categorizes risks based on their primary and secondary categories.

`prioritize_risks(risks: List[Risk]) -> Dict[str, List[Risk]]`
Prioritizes risks based on their impact and likelihood.

`perform_pestel_analysis(risks: List[Risk], external_data: Dict[str, ExternalData]) -> Dict[str, List[Dict[str, str]]]`
Performs a PESTEL analysis of the risks.

`integrate_sasb_materiality(risks: List[Risk], industry: str) -> Dict[str, List[Risk]]`
Integrates SASB materiality assessment for industry-specific risks.

### Scenario Analysis

`simulate_scenario_impact(risks: List[Risk], external_data: Dict[str, ExternalData], scenario: Scenario) -> List[Tuple[Risk, float]]`
Simulates the impact of a given scenario on the provided risks.

`monte_carlo_simulation(risks: List[Risk], external_data: Dict[str, ExternalData], scenarios: Dict[str, Scenario]) -> Dict[str, Dict[int, SimulationResult]]`
Performs Monte Carlo simulations for each risk under different scenarios.

`analyze_scenario_sensitivity(risks: List[Risk], base_scenario: Scenario, variable: str, range_pct: float) -> Dict[str, float]`
Analyzes the sensitivity of risk impacts to changes in a specific scenario variable.

### Interaction Analysis

`analyze_risk_interactions(risks: List[Risk]) -> List[RiskInteraction]`
Analyzes interactions between risks using LLM.

`build_risk_network(risks: List[Risk], interactions: List[RiskInteraction]) -> nx.Graph`
Builds a network graph of risk interactions.

`identify_central_risks(G: nx.Graph) -> Dict[int, float]`
Identifies central risks in the risk network.

### Time Series Analysis

`time_series_analysis(risks: List[Risk], external_data: Dict[str, ExternalData]) -> Dict[int, List[float]]`
Performs time series analysis for each risk, projecting future impacts.

`analyze_impact_trends(time_series_results: Dict[int, List[float]]) -> Dict[int, Dict[str, float]]`
Analyzes trends in the projected risk impacts.

### Advanced Analysis

`conduct_advanced_risk_analysis(risks: List[Risk], scenarios: Dict[str, Scenario], company_industry: str, key_dependencies: List[str], external_data: Dict) -> Dict`
Performs comprehensive risk analysis using various advanced techniques.

`assess_aggregate_impact(risks: List[Risk], interaction_matrix: np.ndarray, num_simulations: int = 1000) -> Dict[str, float]`
Assesses the aggregate impact of all risks, considering their interactions.

`identify_tipping_points(risks: List[Risk], interaction_matrix: np.ndarray) -> List[Dict[str, Any]]`
Identifies potential tipping points in the risk landscape.

### Reporting

`generate_report(risks: List[Risk], ...) -> str`
Generates a comprehensive report in JSON format and creates an HTML version.

`generate_stakeholder_reports(main_report: Dict, company_industry: str) -> Dict[str, str]`
Generates tailored reports for different stakeholder groups.

### Visualization

`generate_visualizations(risks: List[Risk], ...)`
Generates a set of visualizations based on the risk assessment results.

For more detailed information on each function and class, refer to the inline documentation in the source code.