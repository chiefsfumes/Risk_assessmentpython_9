# Testing

## Overview

The testing module ensures the reliability and correctness of the Climate Risk Assessment Tool. It uses the `pytest` framework to run a comprehensive suite of unit tests covering various components of the system.

## Test Structure

The tests are organized in the `tests/` directory, with separate files for each major component of the system:

- `test_data_loader.py`
- `test_risk_analysis.py`
- `test_scenario_analysis.py`
- `test_interaction_analysis.py`
- `test_time_series_analysis.py`
- `test_advanced_analysis.py`
- `test_visualization.py`
- `test_reporting.py`
- `test_pestel_analysis.py`
- `test_sasb_integration.py`
- `test_systemic_risk_analysis.py`

## Running Tests

To run the entire test suite, use the following command from the project root directory:

```bash
pytest
```

To run tests for a specific module:

```bash
pytest tests/test_risk_analysis.py
```

## Key Test Cases

### Data Loading

- Test successful loading of risk data and external data.
- Test error handling for missing files or incorrect data formats.
- Test extraction of risk statements from 10-K filings.

### Risk Analysis

- Test risk categorization and prioritization.
- Verify the correctness of PESTEL analysis.
- Test SASB materiality integration.

### Scenario Analysis

- Verify the correctness of scenario impact calculations.
- Test Monte Carlo simulations for expected distributions.
- Check sensitivity analysis calculations.

### Interaction Analysis

- Test the identification of risk interactions.
- Verify the construction and analysis of the risk network.
- Test the creation and simulation of the risk interaction matrix.

### Time Series Analysis

- Test the ARIMA model projections.
- Verify the identification of critical periods and trends.
- Test cumulative impact forecasting.

### Advanced Analysis

- Test the integration with language models for risk assessment.
- Verify the generation of risk narratives and executive insights.
- Test aggregate impact assessment and tipping point identification.

### Visualization

- Test the generation of various plots and charts.
- Ensure visualizations are saved correctly.

### Reporting

- Test the generation of comprehensive JSON and HTML reports.
- Verify the creation of stakeholder-specific reports.

### Systemic Risk Analysis

- Test the identification of systemic risks and trigger points.
- Verify the calculation of system resilience metrics.

## Example Test Function

Here's an example of a test function from `test_scenario_analysis.py`:

```python
def test_monte_carlo_simulation(sample_risks, sample_external_data, sample_scenarios):
    results = monte_carlo_simulation(sample_risks, sample_external_data, sample_scenarios)
    
    assert len(results) == len(sample_scenarios)
    for scenario_name, scenario_results in results.items():
        assert len(scenario_results) == len(sample_risks)
        for risk_id, sim_result in scenario_results.items():
            assert isinstance(sim_result, SimulationResult)
            assert len(sim_result.impact_distribution) == 1000  # Default NUM_SIMULATIONS
            assert len(sim_result.likelihood_distribution) == 1000
            assert all(0 <= impact <= 1 for impact in sim_result.impact_distribution)
            assert all(0 <= likelihood <= 1 for likelihood in sim_result.likelihood_distribution)
    
    # Test that Net Zero 2050 scenario has lower average impacts than Delayed Transition
    net_zero_impacts = np.mean([np.mean(sim.impact_distribution) for sim in results["Net Zero 2050"].values()])
    delayed_transition_impacts = np.mean([np.mean(sim.impact_distribution) for sim in results["Delayed Transition"].values()])
    assert net_zero_impacts < delayed_transition_impacts
```

## Fixtures

Pytest fixtures are used to provide sample data for tests. For example:

```python
@pytest.fixture
def sample_risks():
    return [
        Risk(id=1, description="Physical Risk 1", category="Physical", likelihood=0.7, impact=0.8, subcategory="Acute", tertiary_category="", time_horizon="Short-term", industry_specific=False, sasb_category=""),
        Risk(id=2, description="Transition Risk 1", category="Transition", likelihood=0.6, impact=0.7, subcategory="Policy", tertiary_category="", time_horizon="Medium-term", industry_specific=True, sasb_category="Energy"),
        Risk(id=3, description="Market Risk 1", category="Market", likelihood=0.5, impact=0.6, subcategory="Demand", tertiary_category="", time_horizon="Long-term", industry_specific=False, sasb_category=""),
    ]
```

## Mocking

For tests that involve external APIs or complex computations, mocking is used to isolate the tested functionality:

```python
@patch('src.risk_analysis.advanced_analysis.openai.ChatCompletion.create')
def test_llm_risk_assessment(mock_create):
    mock_create.return_value.choices[0].message = {'content': 'Mocked LLM response'}
    result = llm_risk_assessment(sample_risk, sample_scenario, "Energy")
    assert "Mocked LLM response" in result
```

## Continuous Integration

The test suite is integrated into the project's CI/CD pipeline, ensuring that all tests pass before changes are merged into the main branch.

## Coverage

To measure test coverage, run:

```bash
pytest --cov=src
```

This command will show the percentage of code covered by tests for each module.

By maintaining a comprehensive test suite, we ensure the reliability and correctness of the Climate Risk Assessment Tool, facilitating confident development and deployment of new features and improvements.