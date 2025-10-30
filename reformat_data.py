import os
import pyarrow as pa
import glob
import re

def save_to_arrow(data, output_file):
    """Saves the data to an Apache Arrow file.

    Args:
        data (dict): A dictionary with two keys: 'problem_statement' and 'output'.
                     Each key contains a list of strings.
        output_file (str): The path to the output Arrow file.
    """
    problem_statement_array = pa.array(data['problem_statement'], type=pa.string())
    output_array = pa.array(data['output'], type=pa.string())
    table = pa.Table.from_arrays([problem_statement_array, output_array], names=['problem_statement', 'output'])
    with pa.OSFile(output_file, 'wb') as sink:
        with pa.RecordBatchFileWriter(sink, table.schema) as writer:
            writer.write_table(table)

def process_learning_file(file_path):
    """Processes a markdown file, splitting it into granular problem/solution pairs based on headings and list items.

    Args:
        file_path (str): The path to the markdown file.

    Returns:
        tuple: A tuple containing two lists: one for problem statements and one for outputs.
    """
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    problems = []
    outputs = []

    lines = content.splitlines()
    current_problem_prefix = []
    current_output_lines = []

    def add_entry():
        if current_problem_prefix and current_output_lines:
            problems.append(" > ".join(current_problem_prefix))
            outputs.append("\n".join(current_output_lines).strip())

    for line in lines:
        if line.startswith('# '): # H1
            add_entry()
            current_problem_prefix = [line[2:].strip()]
            current_output_lines = []
        elif line.startswith('## '): # H2
            add_entry()
            current_problem_prefix = [current_problem_prefix[0], line[3:].strip()] if current_problem_prefix else [line[3:].strip()]
            current_output_lines = []
        elif line.startswith('### '): # H3
            add_entry()
            current_problem_prefix = [current_problem_prefix[0], current_problem_prefix[1], line[4:].strip()] if len(current_problem_prefix) > 1 else [current_problem_prefix[0], line[4:].strip()] if current_problem_prefix else [line[4:].strip()]
            current_output_lines = []
        elif line.startswith('* '): # List item
            add_entry()
            # For list items, we append to the current problem prefix
            # and the output is just the item itself for now, or its sub-content
            item_text = line[2:].strip()
            problems.append(" > ".join(current_problem_prefix + [item_text]))
            current_output_lines = [] # Reset output for new list item
            outputs.append(item_text) # Output is the item itself
        else:
            current_output_lines.append(line)

    add_entry() # Add the last entry

    return problems, outputs

def process_nthw_files(path):
    """Processes all markdown files in the NTHW repository, extracting links as problem/solution pairs.

    Args:
        path (str): The path to the NTHW repository.

    Returns:
        tuple: A tuple containing two lists: one for problem statements and one for outputs.
    """
    problems = []
    outputs = []
    for filename in glob.iglob(os.path.join(path, '**', '*.md'), recursive=True):
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            relative_path = os.path.relpath(filename, path)

            # Extract markdown links: [text](url)
            links = re.findall(r'\[([^\]]+)\]\((https?://[^\)]+)\)', content)
            if links:
                for link_text, link_url in links:
                    problems.append(f"{relative_path} > {link_text}")
                    outputs.append(link_url)
            else:
                # If no links are found, use the entire file content as a single entry
                problems.append(relative_path)
                outputs.append(content)
    return problems, outputs

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--learning_files', nargs='+', default=["/home/julien/termAI/learning_summary.md", "/home/julien/termAI/red_blue_team_skills.md"])
    parser.add_argument('--nthw_path', type=str, default='data/NTHW')
    parser.add_argument('--output_file', type=str, default='data/problem_solution_data.arrow')
    args = parser.parse_args()

    problem_solution_data = {
        'problem_statement': [],
        'output': [],
    }

    # Process learning summary files
    for file in args.learning_files:
        problems, outputs = process_learning_file(file)
        problem_solution_data['problem_statement'].extend(problems)
        problem_solution_data['output'].extend(outputs)

    # Process NTHW files
    problems, outputs = process_nthw_files(args.nthw_path)
    problem_solution_data['problem_statement'].extend(problems)
    problem_solution_data['output'].extend(outputs)

    # Save the data to a new Arrow file
    save_to_arrow(problem_solution_data, args.output_file)

    print(f"Successfully processed data and saved to {args.output_file}")
