import os
import pyarrow as pa

def save_to_arrow(data, output_file):
    """Saves the scraped data to an Apache Arrow file.

    Args:
        data (list): A list of strings, where each string is the content of a scraped website.
        output_file (str): The path to the output Arrow file.
    """
    array = pa.array(data, type=pa.string())
    table = pa.Table.from_arrays([array], names=['content'])
    with pa.OSFile(output_file, 'wb') as sink:
        with pa.RecordBatchFileWriter(sink, table.schema) as writer:
            writer.write_table(table)

if __name__ == '__main__':
    new_file = "/home/julien/termAI/red_blue_team_skills.md"
    output_file = "data/nthw_data.arrow"

    # Read the new file
    with open(new_file, 'r', encoding='utf-8', errors='ignore') as f:
        new_content = f.read()

    # Read existing data
    if os.path.exists(output_file):
        with pa.OSFile(output_file, 'rb') as source:
            existing_table = pa.ipc.open_file(source).read_all()
            existing_data = existing_table.to_pydict()['content']
    else:
        existing_data = []

    # Append new data
    combined_data = existing_data + [new_content]

    # Save combined data
    save_to_arrow(combined_data, output_file)
    print(f"Successfully appended the content of {new_file} to {output_file}")
