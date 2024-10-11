# Reporting

## Overview

The reporting module is responsible for generating comprehensive reports based on the risk assessment results. It produces both a detailed JSON report and a more readable HTML report, catering to different stakeholder needs. Additionally, it generates tailored reports for specific stakeholder groups.

## Key Functions

### `generate_report(risks: List[Risk], categorized_risks: Dict[str, List[Risk]], risk_interactions: List[RiskInteraction], scenario_impacts: Dict[str, List[Tuple[Risk, float]]], simulation_results: Dict[str, Dict[int, SimulationResult]], clustered_risks: Dict[int, List[int]], risk_entities: Dict[str, List[str]], sensitivity_results: Dict[str, Dict[str, float]], time_series_results: Dict[int, List[float]], scenarios: Dict[str, Scenario], advanced_analysis: Dict, systemic_risks: Dict, trigger_points: Dict, resilience_assessment: Dict, monte_carlo_results: Dict, aggregate_impact: Dict, tipping_points: List[Dict]) -> str`

This function generates a comprehensive report in JSON format and also creates an HTML version of the report.

### `generate_stakeholder_reports(main_report: Dict, company_industry: str) -> Dict[str, str]`

This function generates tailored reports for different stakeholder groups based on the main report.

## Report Structure

The generated report includes the following sections:

1. Executive Summary
2. Risk Overview
3. Risk Interactions
4. Scenario Analysis
5. Monte Carlo Results
6. Risk Clusters
7. Sensitivity Analysis
8. Time Series Projection
9. Risk Narratives
10. Executive Insights
11. Mitigation Strategies
12. Systemic Risks
13. Trigger Points
14. Resilience Assessment
15. Aggregate Impact
16. Tipping Points

## Stakeholder Report Types

1. **Board Executive Report**: Focuses on strategic implications and high-level risk overview.
2. **Investor Report**: Emphasizes financial implications and comparative industry analysis.
3. **Regulatory Report**: Details compliance status and risk assessment methodologies.
4. **Public Report**: Provides a simplified overview of the company's climate strategy and key risks.

## Usage Example

```python
# Generate main report
report_json = generate_report(
    risks, categorized_risks, risk_interactions, scenario_impacts,
    simulation_results, clustered_risks, risk_entities, sensitivity_results,
    time_series_results, scenarios, advanced_analysis, systemic_risks,
    trigger_points, resilience_assessment, monte_carlo_results,
    aggregate_impact, tipping_points
)

# Generate stakeholder reports
stakeholder_reports = generate_stakeholder_reports(json.loads(report_json), "Energy")
```

## Key Considerations

- The JSON format allows for easy parsing and integration with other systems or dashboards.
- The HTML report is designed for human readability and can be easily shared with stakeholders who prefer a more visual representation.
- Stakeholder reports are tailored to address the specific concerns and information needs of different groups, enhancing the utility of the risk assessment results.
- The reporting module integrates results from all other modules to provide a comprehensive view of the climate risk landscape.

## Customization

You can customize the reporting by modifying the following in `src/config.py`:

- `OUTPUT_DIR`: Specify the directory for output files
- `REPORT_TEMPLATE`:Specify the HTML template for the report

For more detailed information on the implementation of each function, refer to the source code and inline documentation in `src/reporting.py` and `src/reporting/stakeholder_reports.py`.