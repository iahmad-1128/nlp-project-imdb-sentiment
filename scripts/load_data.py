
import pandas as pd
from pathlib import Path

# Project path
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset path
DATA_FILE = BASE_DIR / "data" / "IMDB Dataset.csv"

# Load dataset
df = pd.read_csv(DATA_FILE)

# Display dataset information
print("Dataset Loaded Successfully!")

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst Five Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSentiment Distribution:")
print(df["sentiment"].value_counts())
