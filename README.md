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

## Free GPU Options for Fine-Tuning

Since Hugging Face Spaces might not always provide GPU access for fine-tuning, here are some alternative free (or free-tier) platforms you can use:

### 1. Google Colab

Google Colab offers free access to GPUs (T4, V100, A100 depending on availability and tier). It's ideal for experimenting and fine-tuning smaller models.

**Instructions:**

1.  **Open a new Colab Notebook:** Go to [Google Colab](https://colab.research.google.com/) and create a new notebook.
2.  **Change Runtime Type:** Go to `Runtime > Change runtime type` and select `GPU` as the hardware accelerator.
3.  **Mount Google Drive (Optional but Recommended):** This allows you to persist your data and models.
    ```python
    from google.colab import drive
    drive.mount('/content/drive')
    # Your project will be accessible at /content/drive/MyDrive/Terminus (or wherever you clone it)
    ```
4.  **Clone the Repository:**
    ```bash
    !git clone https://github.com/Julien-ser/Terminus.git
    %cd Terminus
    ```
5.  **Install Dependencies:**
    ```bash
    !pip install -r requirements.txt
    ```
6.  **Set Hugging Face Token:**
    ```python
    import os
    os.environ["HF_TOKEN"] = "your_hugging_face_token"
    # Or directly in bash: !export HF_TOKEN=your_hugging_face_token
    ```
7.  **Prepare Data (if needed):** If your data is not already in the correct Arrow format, you can run `reformat_data.py`.
    ```bash
    !python3 reformat_data.py --learning_files "/content/drive/MyDrive/path/to/learning_summary.md" "/content/drive/MyDrive/path/to/red_blue_team_skills.md" --nthw_path "/content/drive/MyDrive/path/to/NTHW" --output_file "/content/drive/MyDrive/path/to/problem_solution_data.arrow"
    ```
8.  **Run Fine-Tuning:**
    ```bash
    !python3 fine_tuning.py --dataset_path "/content/drive/MyDrive/path/to/problem_solution_data.arrow"
    ```
9.  **Save Fine-Tuned Model:** The fine-tuned model will be saved to the `output_dir` specified in `config.yaml`. Ensure this path is within your mounted Google Drive if you want to persist it.

### 2. Kaggle Notebooks

Kaggle provides free access to GPUs (P100, T4) for its notebooks, often with longer session times than Colab.

**Instructions:**

1.  **Create a new Kaggle Notebook:** Go to [Kaggle](https://www.kaggle.com/code) and create a new notebook.
2.  **Enable GPU:** In the notebook settings (usually on the right sidebar), set the accelerator to `GPU`.
3.  **Add Data:**
    *   **Upload as Dataset:** For larger datasets, it's best to upload them as a Kaggle Dataset. Then, you can add this dataset to your notebook.
    *   **Direct Upload:** For smaller files, you can upload them directly to the notebook environment.
4.  **Clone the Repository:**
    ```bash
    !git clone https://github.com/Julien-ser/Terminus.git
    %cd Terminus
    ```
5.  **Install Dependencies:**
    ```bash
    !pip install -r requirements.txt
    ```
6.  **Set Hugging Face Token:**
    ```python
    import os
    os.environ["HF_TOKEN"] = "your_hugging_face_token"
    ```
7.  **Prepare Data (if needed):** Adjust paths to your Kaggle input data.
    ```bash
    !python3 reformat_data.py --learning_files "/kaggle/input/your-dataset-name/learning_summary.md" ... --output_file "problem_solution_data.arrow"
    ```
8.  **Run Fine-Tuning:**
    ```bash
    !python3 fine_tuning.py --dataset_path "problem_solution_data.arrow"
    ```
9.  **Save Fine-Tuned Model:** Models saved in the `/kaggle/working/` directory will be available as output files for your notebook.

## License

MIT License.