import numpy as np
import pandas as pd

def monte_carlo_ccp(n, num_simulations):
    results = []

    for _ in range(num_simulations):
        collected = set()
        draws = 0

        while len(collected) < n:
            collected.add(np.random.randint(1, n + 1))
            draws += 1

        results.append(draws)

    df = pd.DataFrame({"simulation": range(1, num_simulations + 1), "draws_needed": results})
    df.to_csv("outputs/monte_carlo_results.csv", index=False)

if __name__ == "__main__":
    monte_carlo_ccp(n=50, num_simulations=10000)