# Data Loading and Preprocessing

## Overview

The data loading and preprocessing module is responsible for importing risk data, external data, and extracting risk statements from 10-K filings. It ensures that the data is properly formatted and ready for analysis.

## Key Functions

### `load_risk_data(file_path: str) -> List[Risk]`

This function loads risk data from a CSV file and converts it into a list of `Risk` objects.

#### Input
- `file_path`: A string representing the path to the CSV file containing risk data.

#### Output
- A list of `Risk` objects.

#### Example

```python
risks = load_risk_data('data/risk_data.csv')
```

### `load_external_data(file_path: str) -> Dict[str, ExternalData]`

This function loads external data from a CSV file and converts it into a dictionary of `ExternalData` objects, keyed by year.

#### Input
- `file_path`: A string representing the path to the CSV file containing external data.

#### Output
- A dictionary with years as keys and `ExternalData` objects as values.

#### Example

```python
external_data = load_external_data('data/external_data.csv')
```

### `extract_risk_statements_from_10k(file_path: str) -> List[Dict[str, str]]`

This function extracts risk statements from a 10-K filing using natural language processing techniques.

#### Input
- `file_path`: A string representing the path to the 10-K filing text file.

#### Output
- A list of dictionaries, each containing a risk statement and associated entities.

#### Example

```python
risk_statements = extract_risk_statements_from_10k('data/10k_filings/company_10k.txt')
```

## Error Handling

All functions include error handling for common issues:

- `FileNotFoundError`: Raised if the specified file does not exist.
- `pd.errors.EmptyDataError`: Raised if the CSV file is empty.
- `ValueError`: Raised if there are issues with data formatting or values.

## Data Models

The module uses the following main data models:

1. `Risk`: Represents a climate risk with attributes such as id, description, category, likelihood, and impact.
2. `ExternalData`: Represents external factors for a given year, including GDP growth, population, energy demand, etc.

These models are defined in the `src/models.py` file and are used throughout the entire project for consistent data representation.

## NLP Processing

The `extract_risk_statements_from_10k` function uses the spaCy library for natural language processing. It performs the following steps:

1. Loads the English NLP model
2. Reads the 10-K filing
3. Extracts the "Risk Factors" section
4. Processes the text with spaCy
5. Identifies sentences likely to contain risk statements
6. Extracts named entities from these sentences

This NLP-based extraction provides an additional source of risk information that can be integrated into the overall risk assessment process.