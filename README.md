# Management of scientific data

Team 8's project for the Management of Scientific Data course at the University of Passau, summer semester 2024. Team: Shirin Shoghli, Sanaz Bayat, Maryam Gheibi, Mozhdeh Ramezani Dastjerdi and Shahrzad Torabi.

We got three published scientific datasets (zipped in `Datasets/`) and had to understand them quickly: what the columns mean, where values are missing or inconsistent, and how the variables relate. The scripts are small because most of the work went into the reports.

- `Implementations/descriptive-statistics.py` loads a dataset and prints a first look.
- `Implementations/inconsistencies_and_plots.py` checks types, compares `PlotID` with `PlotID2`, coerces `Side` to numbers and draws a scatter plot.
- `Implementations/pandas-profiling.py` writes an HTML profile with `ydata-profiling`.
- `Reports/` has the task reports and the profiling report as PDF.

## Running it

```bash
pip install pandas matplotlib ydata-profiling
python Implementations/inconsistencies_and_plots.py
python Implementations/pandas-profiling.py
```

Unzip the datasets first. The scripts still use absolute file paths from our machines, so change the path at the top of each script.
