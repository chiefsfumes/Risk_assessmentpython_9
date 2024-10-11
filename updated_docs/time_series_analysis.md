# Time Series Analysis

## Overview

The time series analysis module projects the future impact of climate risks over time. It uses historical data and statistical techniques to forecast risk trends, identify critical periods, and assess cumulative impacts.

## Key Functions

### `time_series_analysis(risks: List[Risk], external_data: Dict[str, ExternalData]) -> Dict[int, List[float]]`

Performs time series analysis for each risk, projecting future impacts.

### `project_risk_impact_arima(risk: Risk, external_data: Dict[str, ExternalData]) -> List[float]`

Projects the future impact of a single risk using ARIMA (AutoRegressive Integrated Moving Average) modeling.

### `analyze_impact_trends(time_series_results: Dict[int, List[float]]) -> Dict[int, Dict[str, float]]`

Analyzes trends in the projected risk impacts, including slope, average impact, and volatility.

### `identify_critical_periods(time_series_results: Dict[int, List[float]], threshold: float) -> Dict[int, List[int]]`

Identifies periods where projected risk impacts exceed a specified threshold.

### `forecast_cumulative_impact(time_series_results: Dict[int, List[float]]) -> List[float]`

Forecasts the cumulative impact of all risks over time.

## Usage Example

```python
# Load data
risks = load_risk_data('data/risk_data.csv')
external_data = load_external_data('data/external_data.csv')

# Perform time series analysis
time_series_results = time_series_analysis(risks, external_data)

# Analyze impact trends
impact_trends = analyze_impact_trends(time_series_results)

# Identify critical periods
critical_periods = identify_critical_periods(time_series_results, threshold=0.7)

# Forecast cumulative impact
cumulative_impact = forecast_cumulative_impact(time_series_results)
```

## Key Considerations

- The module uses ARIMA modeling for sophisticated time series forecasting.
- Historical external data is used to inform future projections.
- Trend analysis helps identify risks that are expected to worsen or improve over time.
- Critical period identification aids in pinpointing times of heightened risk.
- Cumulative impact forecasting provides a holistic view of overall risk progression.

## Customization

You can customize the time series analysis by modifying the following in `src/config.py`:

- `TIME_SERIES_HORIZON`: Set the number of future time periods to project
- `CRITICAL_IMPACT_THRESHOLD`: Define the threshold for identifying critical periods

## Visualization

The results of the time series analysis can be visualized using functions in the visualization module:

- `time_series_projection`: Plots the projected impact of each risk over time
- `cumulative_impact_plot`: Visualizes the forecasted cumulative impact of all risks

These visualizations help in understanding the temporal dynamics of climate risks and identifying key trends and critical points in the future.

For more detailed information on the implementation of each function, refer to the source code and inline documentation in `src/risk_analysis/time_series_analysis.py`.