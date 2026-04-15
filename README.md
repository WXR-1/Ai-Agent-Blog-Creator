# CrewAI Content Research & Writing Pipeline

This project demonstrates CrewAI automating a content creation workflow using 4 specialized agents with open source LLMs.

## Use Case: Automated Blog Post Generation

The system automatically:
1. **Researches** a given topic
2. **Writes** engaging content based on research
3. **Fact-checks** claims in the content
4. **Edits** and polishes the final output

## Architecture

### 4 Agents:

1. **Research Agent** - Gathers information and researches topics
2. **Content Writer** - Creates engaging, well-structured blog posts
3. **Fact Checker** - Validates claims and ensures accuracy
4. **Editor** - Reviews, polishes, and improves readability

### Tasks Flow:

```
Topic Input
    ↓
[Research Agent] → Research Report
    ↓
[Content Writer] → Draft Blog Post
    ↓
[Fact Checker] → Validation Report
    ↓
[Editor] → Final Polished Content
    ↓
Output
```

## Setup Instructions

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Project

```bash
python main.py
```

## Configuration

### Using Open Source LLMs

This project is configured to use open source LLMs. You have several options:

#### Option 1: Ollama (Local)
1. Install Ollama from https://ollama.ai
2. Run: `ollama pull mistral` or `ollama pull neural-chat`
3. Update config in `main.py` to use Ollama endpoint

#### Option 2: Hugging Face (Free API)
1. Get free API key from https://huggingface.co
2. Update environment variables

#### Option 3: LM Studio (Local GUI)
1. Download from https://lmstudio.ai
2. Load a model and enable local API
3. Point agents to local endpoint

## Project Structure

```
.
├── main.py                 # Entry point and crew setup
├── requirements.txt        # Python dependencies
├── agents/
│   ├── __init__.py
│   ├── researcher.py       # Research agent definition
│   ├── writer.py           # Content writer agent
│   ├── fact_checker.py     # Fact checking agent
│   └── editor.py           # Editing agent
├── tasks/
│   ├── __init__.py
│   ├── research_task.py    # Research task
│   ├── writing_task.py     # Writing task
│   ├── checking_task.py    # Fact-checking task
│   └── editing_task.py     # Editing task
└── config.py               # Configuration and LLM setup
```

## Example Usage

```python
from main import content_crew

result = content_crew.kickoff(inputs={
    "topic": "Artificial Intelligence in Healthcare",
    "style": "informative and engaging"
})

print(result)
```

## Output

The final output is a fully researched, written, fact-checked, and edited blog post ready for publication.

## Notes

- CrewAI handles agent coordination and communication
- Each agent can use different prompts and tools
- The pipeline is fully automated end-to-end
- Agents can iterate and refine outputs
