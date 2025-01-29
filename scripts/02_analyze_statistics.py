# 02_analyze_statistics.py
# Analyze the statistical properties of CCP data

# Import necessary libraries (pandas, scipy.stats, numpy)
# Read `outputs/simulation_data.csv`
# Compute key statistics:
#   - Mean, median, standard deviation
#   - 95% confidence interval for expected draws
#   - Compare empirical results to theoretical expectation `n * Hn`
# Save results to `outputs/analysis_results.json`