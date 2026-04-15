# QUICKSTART GUIDE

## 🚀 Getting Started

### 1. Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### 2. Choose Your LLM

All you need to do is edit `config.py` and change the `LLM_CHOICE` variable at the top:

```python
LLM_CHOICE = "ollama"  # Change this to your desired LLM
```

#### Option A: Ollama (Recommended - Completely Free & Local)
```bash
# 1. Install Ollama from https://ollama.ai
# 2. Run this command in a terminal:
ollama pull mistral

# 3. Keep that terminal open (server runs on localhost:11434)

# 4. In config.py, set:
LLM_CHOICE = "ollama"
```

#### Option B: Hugging Face (Free Tier + Paid)
```bash
# 1. Sign up at https://huggingface.co
# 2. Create an API key: https://huggingface.co/settings/tokens
# 3. Save your token to a .env file or environment variable:
set HF_API_KEY=your_token_here    # Windows
# OR
export HF_API_KEY=your_token_here # macOS/Linux

# 4. In config.py, set:
LLM_CHOICE = "huggingface"
```

#### Option C: LM Studio (Completely Free & Local)
```bash
# 1. Download LM Studio from https://lmstudio.ai
# 2. Load a model (Mistral or similar)
# 3. Click "Local Server" to enable the API
# 4. In config.py, set:
LLM_CHOICE = "lm_studio"
```

#### Option D: OpenAI (Paid)
```bash
# 1. Get API key from https://platform.openai.com/account/api-keys
# 2. Set environment variable:
set OPENAI_API_KEY=your_key_here    # Windows
# OR
export OPENAI_API_KEY=your_key_here # macOS/Linux

# 3. In config.py, set:
LLM_CHOICE = "openai"
```

### 3. Run the Pipeline

```bash
# Run with default example
python main.py

# Or run a specific example
python examples.py tech_trends
python examples.py health
python examples.py business
python examples.py education

# Or modify main.py with your own topic
```

## 📊 What Happens

The pipeline runs 4 agents sequentially:

1. **🔍 Researcher** - Researches the topic thoroughly
2. **✍️  Writer** - Creates engaging blog post content  
3. **✔️  Fact-Checker** - Validates claims and accuracy
4. **🎯 Editor** - Polishes and refines the output

Final output is saved to `output.md`

## 💡 Key Features

- ✅ **No coding required** - Just provide a topic
- ✅ **Completely automated** - 4 agents collaborate
- ✅ **Open source LLMs** - Use Ollama, HF, or LM Studio
- ✅ **Flexible** - Works with any topic
- ✅ **Publication-ready** - Output is fact-checked and polished
- ✅ **Extensible** - Easy to add more agents or customize

## 🔧 Troubleshooting

### Ollama not responding
- Make sure Ollama is running: `ollama serve` in a terminal
- Check: http://localhost:11434/api/models

### Hugging Face rate limited
- Upgrade to paid account or wait 24h
- Or switch to Ollama (local, unlimited)

### Low quality output
- Use a larger model: `ollama pull neural-chat`
- Give clearer topic descriptions
- Adjust agent backstories in `agents/` files

## 📝 Next Steps

- Modify agent backstories in `agents/` folder
- Customize task descriptions in `tasks/` folder
- Add custom tools to agents
- Extend pipeline with more agents

