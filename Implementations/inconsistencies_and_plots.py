import zipfile
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

DATASET = Path(__file__).resolve().parent.parent / "Datasets" / "24246_2_Dataset.zip"

# Read the data sheet straight from the zipped dataset in Datasets/
df = pd.read_excel(zipfile.ZipFile(DATASET).open("24246_2_data.xlsx"))

# Display the first few rows of the DataFrame
print(df.head())

# Display information about the DataFrame
df.info()

# Check for inconsistencies
inconsistencies = df[df["PlotID"] != df["PlotID2"]]

# Convert the "Side" column to numeric, handling errors
df["Side"] = pd.to_numeric(df["Side"], errors="coerce")

# Find negative values in the "Side" column
negative_values = df[df["Side"] < 0]

# Scatter plot
plt.scatter(df["PredationMark"], df["PredationMark"])

plt.xlabel("PredationMark")
plt.ylabel("PredationMark2")
plt.title("Scatter Plot of PredationMark vs PredationMark2")
plt.show()
