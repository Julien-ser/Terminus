import pyarrow as pa
import pandas as pd

# Read the Arrow file
with pa.OSFile('data/nthw_data.arrow', 'rb') as source:
    table = pa.ipc.open_file(source).read_all()

# Convert the table to a pandas DataFrame
df = table.to_pandas()

# Print the first 10 rows of the 'content' column
for i, row in enumerate(df['content'].head(10)):
    print(f"--- Entry {i+1} ---")
    print(row)
    print("\n")

