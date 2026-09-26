import zipfile
from pathlib import Path

import pandas as pd

DATASET = Path(__file__).resolve().parent.parent / "Datasets" / "24246_2_Dataset.zip"

# Read the data sheet straight from the zipped dataset in Datasets/
df = pd.read_excel(zipfile.ZipFile(DATASET).open("24246_2_data.xlsx"))

# Display the first few rows of the DataFrame to verify the data has been loaded
print(df.head())
