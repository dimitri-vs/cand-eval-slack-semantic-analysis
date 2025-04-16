# Slack Channel LLM Sentiment Analysis for Project Health

This project serves as a candidate evaluation task, simulating a real-world scenario to assess skills in prompt engineering and interacting with Large Language Models (LLMs).

The goal is to build a proof-of-concept of an internal tool that would analyze Slack channel conversations specific to client projects. Input will typically consist of anonymized message excerpts (representing roughly a two weeks of communication), provided as Markdown files within the `data/` directory. By performing semantic analysis on these excerpts, the tool would assess the overall sentiment or "temperature" of the project discussions.

The core output should distill essential insights for project or account managers, potentially highlighting areas requiring attention and suggesting possible interventions. The output must also include the LLM's reasoning (a brief explanation of *why* it generated the specific analysis and suggestions) to ensure transparency and understand the model's decision-making process. The final analysis should be clearly presented, for instance, by printing structured output to the console.

The final deliverable is a script that takes the sample messages, executes the analysis prompt against an LLM, and presents the analysis, insights, potential interventions, and reasoning.

## Project Structure

```
├── src/                # Source code
│   └── processor.py    # Your main script
├── data/               # Input markdown files
│   ├── input1.md
│   └── input2.md
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Running & Developing the Project Locally

### Initial Setup
Requires Python 3.9 or higher (check with `python --version`)
Requires `uv` CLI tool (https://docs.astral.sh/uv/getting-started/#installation)
- Create a virtual environment using `uv venv --python ">=3.9"`
- Always run `.venv\Scripts\activate` to activate the virtual environment (setup your IDE to do it automatically)
- Run `uv pip install -r requirements.txt` to install all dependencies

### Ongoing Development
- Run `.venv\Scripts\activate` to activate the virtual environment
- ⚠️ Always activate the virtual environment before running any commands
- To check for package updates, run `pip list --outdated`
- To add new packages, first add it to `requirements.txt` then run `uv pip install -r requirements.txt`

### Running the Analysis
- Ensure your virtual environment is activated (`.venv\Scripts\activate`).
- Run the script, passing the input data file as an argument:
  ```powershell
  python src/processor.py data/input1.md
  ```