import pyarrow as pa
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file_path', type=str, default='data/problem_solution_data.arrow')
args = parser.parse_args()

# Read the Arrow file
with pa.OSFile(args.file_path, 'rb') as source:
    table = pa.ipc.open_file(source).read_all()

# Convert the table to a pandas DataFrame
df = table.to_pandas()

# Print the first 5 problem/solution pairs
for i in range(min(5, len(df))):
    print(f"--- Example {i+1} ---")
    print(f"Problem Statement: {df['problem_statement'].iloc[i]}")
    print(f"Output: {df['output'].iloc[i]}")
    print("\n")
