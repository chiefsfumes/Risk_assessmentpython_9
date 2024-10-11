# Troubleshooting Guide

## Common Issues and Solutions

### 1. ImportError: No module named 'openai'

**Problem**: The OpenAI library is not installed.

**Solution**: 
```
pip install openai
```

### 2. FileNotFoundError: [Errno 2] No such file or directory: 'data/risk_data.csv'

**Problem**: The risk data file is missing or in the wrong location.

**Solution**: Ensure that 'risk_data.csv' is present in the 'data' directory. Check the file path in the configuration.

### 3. KeyError: 'OPENAI_API_KEY'

**Problem**: The OpenAI API key is not set in the environment variables.

**Solution**: Set the API key in your .env file or export it as an environment variable:
```
export OPENAI_API_KEY=your_api_key_here
```

### 4. ValueError: could not convert string to float: 'N/A'

**Problem**: The CSV data contains non-numeric values in numeric fields.

**Solution**: Clean your input data, ensuring all numeric fields contain valid numbers. Replace 'N/A' with an appropriate numeric value or handle it in the data loading function.

### 5. MemoryError during Monte Carlo simulation

**Problem**: The simulation is using too much memory, possibly due to a large number of risks or scenarios.

**Solution**: Reduce the number of simulations (NUM_SIMULATIONS in config.py) or process risks in batches.

### 6. RuntimeError: CUDA out of memory

**Problem**: GPU memory is exhausted during language model operations.

**Solution**: Reduce batch size for LLM operations or switch to CPU-only mode by setting `device='cpu'` in the LLM configuration.

### 7. JSONDecodeError: Expecting value: line 1 column 1 (char 0)

**Problem**: The JSON report file is empty or corrupted.

**Solution**: Check the `generate_report` function for any issues that might prevent proper JSON generation. Ensure all data inputs are valid.

### 8. NetworkXError: Graph is empty.

**Problem**: The risk network graph is empty, possibly due to no risk interactions being identified.

**Solution**: Check the `analyze_risk_interactions` function and ensure that risks are being properly processed and interactions are being identified.

## Performance Optimization

If the tool is running slowly:

1. Reduce the number of Monte Carlo simulations
2. Use a smaller subset of risks for initial analysis
3. Optimize data structures (e.g., use numpy arrays instead of lists for large datasets)
4. Consider using multiprocessing for parallel computation of independent tasks
5. Profile the code to identify bottlenecks:
   ```python
   import cProfile
   cProfile.run('main()')
   ```

## Debugging Tips

1. Enable debug logging:
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

2. Use print statements or logging to track progress through long-running functions

3. For LLM-related issues, print out the prompts being sent to ensure they're formatted correctly

4. Use a debugger like pdb or an IDE's built-in debugger to step through code:
   ```python
   import pdb; pdb.set_trace()
   ```

## Updating Dependencies

If you encounter compatibility issues, try updating the project dependencies:

```bash
pip install --upgrade -r requirements.txt
```

## Getting Help

If you encounter issues not covered here:

1. Check the project's issue tracker on GitHub for similar problems and solutions
2. Consult the [API Reference](api_reference.md) for correct usage of functions
3. Review the [Contributing Guide](contributing.md) for guidelines on reporting issues
4. Reach out to the maintainers or community forums for support

Remember to provide detailed information about your environment, input data, and the full error traceback when seeking help.