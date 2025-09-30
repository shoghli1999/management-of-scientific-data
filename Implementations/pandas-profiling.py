import pandas as pd
from ydata_profiling import ProfileReport
# from pydantic_settings import BaseSettings
# from pandas_profiling.config import Correlation, Settings

# Read the dataset
df = pd.read_csv("/home/maryam/Management/24246_2_Dataset/24246_2_data.csv")

# Create a ProfileReport
profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)

# Save the report to an HTML file
profile.to_file("/home/maryam/Management/output_report.html")

# Display the report in a Jupyter Notebook
profile.to_notebook_iframe()
