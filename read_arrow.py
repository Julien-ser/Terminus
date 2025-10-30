import pyarrow as pa
import pandas as pd

# Read the Arrow file
with pa.OSFile('data/problem_solution_data.arrow', 'rb') as source:
    table = pa.ipc.open_file(source).read_all()

# Convert the table to a pandas DataFrame
df = table.to_pandas()

# Print the first 5 problem/solution pairs
for i in range(min(5, len(df))):
    print(f"--- Example {i+1} ---")
    print(f"Problem Statement: {df['problem_statement'].iloc[i]}")
    print(f"Output: {df['output'].iloc[i]}")
    print("\n")
