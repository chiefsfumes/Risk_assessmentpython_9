# Getting Started with the Climate Risk Assessment Tool

## Overview
This guide will help you set up and run the Climate Risk Assessment Tool for the first time.

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for version control)

## Installation

1. Clone the repository (if using Git):
   ```
   git clone https://github.com/your-repo/climate-risk-assessment-tool.git
   cd climate-risk-assessment-tool
   ```

   Or download and extract the project zip file.

2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Running the Tool

1. Prepare your input data:
   - Place your risk data CSV in `data/risk_data.csv`
   - Place your external data CSV in `data/external_data.csv`
   - (Optional) Place 10-K filings in `data/10k_filings/` for NLP risk extraction

2. Run the main script:
   ```
   python src/main.py
   ```

3. Find the output:
   - JSON report: `output/climate_risk_report.json`
   - HTML report: `output/climate_risk_report.html`
   - Visualizations: `output/*.png`
   - Stakeholder reports: `output/*_report.json`

## Configuration

You can customize the tool's behavior by modifying `src/config.py`. Key configurations include:

- `SCENARIOS`: Define different climate scenarios
- `NUM_SIMULATIONS`: Set the number of Monte Carlo simulations
- `TIME_SERIES_HORIZON`: Set the number of years for time series projections
- `LLM_MODEL`: Specify the language model for advanced analysis

## Next Steps
- Review the [Configuration](configuration.md) guide for detailed customization options
- Explore the [Risk Analysis](risk_analysis.md) documentation to understand the analysis process
- Check out the [Visualization](visualization.md) and [Reporting](reporting.md) guides for interpreting results
- For advanced usage, refer to the [API Reference](api_reference.md)

## Troubleshooting

If you encounter any issues, please refer to the [Troubleshooting](troubleshooting.md) guide or open an issue on the project's GitHub repository.