import zipfile
from pathlib import Path

import pandas as pd
from ydata_profiling import ProfileReport

# from pydantic_settings import BaseSettings
# from pandas_profiling.config import Correlation, Settings

DATASET = Path(__file__).resolve().parent.parent / "Datasets" / "24246_2_Dataset.zip"

# Read the data sheet straight from the zipped dataset in Datasets/
df = pd.read_excel(zipfile.ZipFile(DATASET).open("24246_2_data.xlsx"))

# Create a ProfileReport
profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)

# Save the report to an HTML file
profile.to_file(DATASET.parent.parent / "output_report.html")

# In a Jupyter notebook, profile.to_notebook_iframe() shows the report inline
