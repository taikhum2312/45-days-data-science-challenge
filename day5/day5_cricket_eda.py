"""
Cricket Match Exploratory Data Analysis (EDA)
This script processes cricket match data to analyze winning patterns, 
home/away advantages, and team performance metrics.
"""

import pandas as pd
import matplotlib.pyplot as plt

# --- 1. DATA LOADING ---
print("Initializing EDA...")
try:
    # Loading the dataset with tab separator as identified in the original script
    df = pd.read_csv("day5/cricket_data.csv", sep="\t")
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: The file 'cricket_data.csv' was not found in the 'day5/' directory.")
    exit()

# --- 2. DATA INSPECTION ---
print("\n--- Basic Dataset Info ---")
print(f"Shape: {df.shape}")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# --- 3. FEATURE ENGINEERING ---

# Create a 'win_type' column to categorize how matches were won
# Logic: If 'win_by_runs' is present, category is Runs; if 'win_by_wickets', category is Wickets.
df["win_type"] = df.apply(
    lambda row: "Runs" if pd.notnull(row["win_by_runs"]) 
    else ("Wickets" if pd.notnull(row["win_by_wickets"]) else "Other"),
    axis=1
)

# Identify if the winner was the 'Home' team or 'Away' team
# This creates a boolean series (True/False)
df["home_win"] = df["winner"] == df["home"]
df["away_win"] = df["winner"] == df["away"]

# --- 4. DATA CLEANING ---

# Create a filtered version of the dataframe excluding matches with no results (Null winners)
df_valid = df[df["winner"].notnull()]

# --- 5. DATA ANALYSIS ---

# 5.1 Home vs Away Win Rates
# .mean() on a boolean column gives the percentage of True values (rate)
home_win_rate_valid = (df_valid["Winner"] == df_valid["home"]).mean()
away_win_rate_valid = (df_valid["winner"] == df_valid["away"]).mean()

print(f"\nHome Win Rate: {home_win_rate_valid:.2%}")
print(f"Away Win Rate: {away_win_rate_valid:.2%}")

# 5.2 Problem Row Identification
# Identify matches where the winner listed is neither the home nor the away team
# This often highlights data entry errors or neutral venue matches
problem_rows = df_valid[
    ~(
        (df_valid["winner"] == df_valid["home"]) |
        (df_valid["winner"] == df_valid["away"])
    )
]

print(f"\nFound {len(problem_rows)} matches with inconsistent winner data.")
if not problem_rows.empty:
    print("Sample of problematic rows:")
    print(problem_rows[["home", "away", "winner"]].head(10))

# 5.3 Specific Team Analysis (Example: Western Teams)
# Using string contains to find specific regional teams
print("\n--- 'Western' Team Appearances vs Wins ---")
western_home = df["home"].value_counts().loc[lambda x: x.index.str.contains("Western")]
western_wins = df["winner"].value_counts().loc[lambda x: x.index.str.contains("Western")]
print(f"Appearances as Home Team:\n{western_home}")
print(f"Total Match Wins:\n{western_wins}")

# 5.4 Top Performing Teams
print("\n--- Top 10 Teams by Total Wins ---")
team_win_counts = df_valid["winner"].value_counts().head(10)
win_percentage = (team_win_counts / len(df_valid)) * 100
print(pd.DataFrame({'Total Wins': team_win_counts, 'Win %': win_percentage}))

# --- 6. FINAL CLEANUP ---
# Check for duplicates
print(f"\nDuplicate rows found: {df.duplicated().sum()}")