import pyarrow as pa

output_file = "data/problem_solution_data.arrow"

with pa.OSFile(output_file, 'rb') as source:
    table = pa.ipc.open_file(source).read_all()

print(f"The Arrow file has {table.num_rows} cases.")
