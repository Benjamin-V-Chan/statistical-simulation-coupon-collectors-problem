import numpy as np
import pandas as pd

def expected_steps(n):
    return n * sum(1 / i for i in range(1, n + 1))

def markov_analysis():
    n_values = range(10, 101, 10)
    results = [{"n": n, "expected_steps": expected_steps(n)} for n in n_values]
    
    df = pd.DataFrame(results)
    df.to_csv("outputs/markov_results.csv", index=False)

if __name__ == "__main__":
    markov_analysis()