import pyarrow as pa
import pandas as pd

# Read the Arrow file
with pa.OSFile('data/nthw_data.arrow', 'rb') as source:
    table = pa.ipc.open_file(source).read_all()

# Convert the table to a pandas DataFrame
df = table.to_pandas()

# Get the last 21 rows
linux_data = df.tail(21)

# Print the content of the first of the last 21 rows
print(linux_data['content'].iloc[0])

