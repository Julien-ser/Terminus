import pyarrow as pa
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file_path', type=str, default='data/problem_solution_data.arrow')
args = parser.parse_args()

output_file = args.file_path

with pa.OSFile(output_file, 'rb') as source:
    table = pa.ipc.open_file(source).read_all()

print(f"The Arrow file has {table.num_rows} cases.")
