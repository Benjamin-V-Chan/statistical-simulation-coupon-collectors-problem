import numpy as np
import pandas as pd
import random

def simulate_coupon_collection(n, num_trials):
    results = []
    
    for _ in range(num_trials):
        collected = set()
        draws = 0
        
        while len(collected) < n:
            collected.add(random.randint(1, n))
            draws += 1
        
        results.append(draws)

    df = pd.DataFrame({"trial": range(1, num_trials + 1), "draws_needed": results})
    df.to_csv("outputs/simulation_data.csv", index=False)

if __name__ == "__main__":
    simulate_coupon_collection(n=50, num_trials=10000)