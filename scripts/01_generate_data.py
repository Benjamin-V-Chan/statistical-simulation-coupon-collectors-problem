# 01_generate_data.py
# Simulate the Coupon Collector's Problem and generate raw data

# Import necessary libraries (numpy, pandas, random)
# Define a function `simulate_coupon_collection(n, num_trials)`
#   - n: number of unique coupons
#   - num_trials: number of simulations
#   - Output: DataFrame with collected coupons for each trial

#   For each trial:
#       - Initialize a set to track collected coupons
#       - Keep drawing random coupons until all `n` are collected
#       - Record the number of draws required

#   Convert results into a DataFrame and save to `outputs/simulation_data.csv`

# If script is run as main, execute the simulation with default parameters