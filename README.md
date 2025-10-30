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
   python3 fine_tuning.py
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

## Contributing

Fork, create a branch, commit changes, and submit a PR. Follow the existing code style.

## License

MIT License.