import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_results():
    df = pd.read_csv("outputs/simulation_data.csv")

    plt.figure(figsize=(8, 5))
    sns.histplot(df["draws_needed"], bins=30, kde=True)
    plt.title("Distribution of Draws Needed")
    plt.savefig("outputs/visualizations/histogram.png")
    
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df["draws_needed"])
    plt.title("Boxplot of Draws Needed")
    plt.savefig("outputs/visualizations/boxplot.png")

if __name__ == "__main__":
    visualize_results()