# Terminus

A terminal-based AI agent for cybersecurity, fine-tuned on curated datasets to assist with CTF challenges, admin tasks, and real-world security problems.

## Installation

1. Clone the repo:
   ```
   git clone https://github.com/Julien-ser/Terminus.git
   cd Terminus
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt  # If you create one, or manually install: torch, transformers, langchain, pyarrow, etc.
   ```

3. Set environment variables:
   ```
   export HF_TOKEN=your_hugging_face_token  # For Llama model access
   ```

## Usage

1. **Fine-Tune the Model** (optional, if not done):
   ```
   python3 fine_tuning.py --dataset_path /path/to/your/data.arrow
   ```

2. **Run the Agentic Terminal**:
   ```
   python3 terminal_agent.py
   ```
   Type queries like "Solve this CTF challenge" or "Check system logs"—the agent will reason and execute commands.

3. **TUI Mode**:
   ```
   python3 tui_agent.py
   ```

## Data

- `data/NTHW/`: Cybersecurity resources from Not The Hidden Wiki.
- `data/*.arrow`: Processed problem-solution datasets.

## Scripts Overview

- `terminal_agent.py`: Main agent interface.
- `fine_tuning.py`: Fine-tune Llama3-1B on your data.
- `reformat_data.py`: Convert markdown to Arrow format.
- `analyze_arrow.py`: Inspect data.

## Script Arguments

Many of the Python scripts in this project now accept command-line arguments to specify file paths. This makes them more flexible and easier to use in different environments. Here is a list of the scripts and their arguments:

- `fine_tuning.py`:
  - `--dataset_path`: Path to the Arrow data file for training (default: `data/problem_solution_data.arrow`).

- `analyze_arrow.py`:
  - `--file_path`: Path to the Arrow file to analyze (default: `data/nthw_data.arrow`).

- `count_arrow_rows.py`:
  - `--file_path`: Path to the Arrow file to count rows in (default: `data/problem_solution_data.arrow`).

- `read_arrow.py`:
  - `--file_path`: Path to the Arrow file to read (default: `data/problem_solution_data.arrow`).

- `read_linux_data.py`:
  - `--file_path`: Path to the Arrow file to read (default: `data/nthw_data.arrow`).

- `reformat_data.py`:
  - `--learning_files`: Paths to the learning summary files (default: `["/home/julien/termAI/learning_summary.md", "/home/julien/termAI/red_blue_team_skills.md"]`).
  - `--nthw_path`: Path to the NTHW repository (default: `data/NTHW`).
  - `--output_file`: Path to the output Arrow file (default: `data/problem_solution_data.arrow`).

- `scraper.py`:
  - `--new_file`: Path to the new file to append to the Arrow file (default: `/home/julien/termAI/red_blue_team_skills.md`).
  - `--output_file`: Path to the output Arrow file (default: `data/nthw_data.arrow`).

## Contributing

Fork, create a branch, commit changes, and submit a PR. Follow the existing code style.

## License

MIT License.