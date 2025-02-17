import pandas as pd

# Load the CSV files
files = ["file1.csv", "file2.csv"]  # Replace with actual file names
count = 0

for file in files:
    df = pd.read_csv(file)
    count += df.apply(lambda row: row.astype(str).str.contains("GitHub", case=False).any(), axis=1).sum()

print(f"Total lines containing 'GitHub': {count}")
