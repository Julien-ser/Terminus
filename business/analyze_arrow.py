import pyarrow as pa
import pandas as pd
import argparse

# Read the Arrow file
parser = argparse.ArgumentParser()
parser.add_argument('--file_path', type=str, default='data/nthw_data.arrow')
args = parser.parse_args()

with pa.OSFile(args.file_path, 'rb') as source:
    table = pa.ipc.open_file(source).read_all()

# Convert the table to a pandas DataFrame
df = table.to_pandas()

# Print the first 10 rows of the 'content' column
for i, row in enumerate(df['content'].head(10)):
    print(f"--- Entry {i+1} ---")
    print(row)
    print("\n")
