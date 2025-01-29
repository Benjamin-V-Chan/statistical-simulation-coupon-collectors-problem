import pandas as pd
import numpy as np
import json
from scipy.stats import sem, norm

def analyze_statistics():
    df = pd.read_csv("outputs/simulation_data.csv")
    n = 50  
    h_n = sum(1 / i for i in range(1, n + 1))  
    expected_draws = n * h_n  
    
    mean_draws = df["draws_needed"].mean()
    std_draws = df["draws_needed"].std()
    conf_interval = norm.interval(0.95, loc=mean_draws, scale=sem(df["draws_needed"]))

    results = {
        "mean": mean_draws,
        "std_dev": std_draws,
        "95%_confidence_interval": conf_interval,
        "expected_draws": expected_draws
    }
    
    with open("outputs/analysis_results.json", "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    analyze_statistics()