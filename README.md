# statistical-simulation-coupon-collectors-problem

## Project Overview

The Coupon Collector's Problem (CCP) is a classic problem in probability theory and statistics that models the process of collecting distinct items randomly. Given a total of \( n \) unique coupons, we ask: how many draws are needed, on average, to collect all \( n \) coupons at least once?

## Folder Structure

```
project-root/
├── scripts/
│   ├── 01_generate_data.py      # Simulate and generate CCP data
│   ├── 02_analyze_statistics.py # Analyze statistical properties
│   ├── 03_visualize_results.py  # Generate visualizations
│   ├── 04_monte_carlo_sim.py    # Monte Carlo analysis
│   ├── 05_markov_analysis.py    # Markov chain analysis
├── outputs/                     # Store results
│   ├── simulation_data.csv
│   ├── analysis_results.json
│   ├── visualizations/
│   ├── monte_carlo_results.csv
│   ├── markov_results.csv
├── README.md
├── requirements.txt             # Required Python packages
```

---

## Usage

### 1. Setup the Project:

Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 2. Run the Scripts

#### Generate CCP Simulation Data
```bash
python scripts/01_generate_data.py
```
This script simulates the coupon collection process and stores results in `outputs/simulation_data.csv`.

#### Analyze Statistical Properties
```bash
python scripts/02_analyze_statistics.py
```
Computes mean, variance, confidence intervals, and theoretical comparison, saving results in `outputs/analysis_results.json`.

#### Generate Visualizations
```bash
python scripts/03_visualize_results.py
```
Creates a histogram and boxplot of the required draws, stored in `outputs/visualizations/`.

#### Monte Carlo Analysis
```bash
python scripts/04_monte_carlo_sim.py
```
Runs Monte Carlo trials to estimate CCP behavior, saving data to `outputs/monte_carlo_results.csv`.

#### Markov Chain Model Analysis
```bash
python scripts/05_markov_analysis.py
```
Computes the expected number of steps using Markov chains and saves results to `outputs/markov_results.csv`.

---

## Requirements

Install dependencies before running scripts:

```
numpy
pandas
matplotlib
seaborn
scipy
```