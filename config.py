"""
LLM Configuration for CrewAI with Open Source Models

This file configures environment variables for CrewAI to use different LLM backends.
CrewAI will automatically use these settings for all agents.

Options:
1. Ollama (local) - Free, runs locally
2. Hugging Face Inference API - Free tier available
3. LM Studio - Local GUI-based LLM runner
4. OpenAI - Cloud-based, requires API key
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ============================================
# SELECT YOUR LLM HERE
# ============================================
# Change this to select which LLM to use:
LLM_CHOICE = "ollama"  # Options: "ollama", "huggingface", "lm_studio", "openai"

# ============================================
# Configure Environment Variables
# ============================================

if LLM_CHOICE == "ollama":
    """
    Using Ollama (Recommended - Free & Local)
    
    Prerequisites:
    - Install Ollama from https://ollama.ai
    - Run: ollama pull mistral
    - Keep Ollama running: ollama serve
    """
    os.environ["OPENAI_API_KEY"] = "ollama"
    os.environ["OPENAI_API_BASE"] = "http://localhost:11434/v1"
    os.environ["OPENAI_MODEL_NAME"] = "mistral"
    
elif LLM_CHOICE == "huggingface":
    """
    Using Hugging Face (Free API - with rate limits)
    
    Prerequisites:
    - Get API key from https://huggingface.co/settings/tokens
    - Set HF_API_KEY environment variable
    """
    hf_token = os.getenv("HF_API_KEY")
    if not hf_token:
        raise ValueError(
            "HF_API_KEY environment variable not set. "
            "Get it from https://huggingface.co/settings/tokens"
        )
    os.environ["OPENAI_API_KEY"] = hf_token
    os.environ["OPENAI_API_BASE"] = "https://api-inference.huggingface.co"
    os.environ["OPENAI_MODEL_NAME"] = "mistralai/Mistral-7B-Instruct-v0.1"
    
elif LLM_CHOICE == "lm_studio":
    """
    Using LM Studio (Free - Local GUI)
    
    Prerequisites:
    - Download from https://lmstudio.ai
    - Load a model and enable "Local Server"
    - Runs on localhost:1234
    """
    os.environ["OPENAI_API_KEY"] = "lm-studio"
    os.environ["OPENAI_API_BASE"] = "http://localhost:1234/v1"
    os.environ["OPENAI_MODEL_NAME"] = "mistral"
    
elif LLM_CHOICE == "openai":
    """
    Using OpenAI API (Paid)
    
    Prerequisites:
    - Set OPENAI_API_KEY environment variable
    - API key from https://platform.openai.com/account/api-keys
    """
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError(
            "OPENAI_API_KEY environment variable not set. "
            "Get it from https://platform.openai.com/account/api-keys"
        )
    os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"
    
else:
    raise ValueError(f"Unknown LLM choice: {LLM_CHOICE}")

# ============================================
# Utility function for debugging
# ============================================
def get_current_config():
    """Returns the current LLM configuration."""
    return {
        "choice": LLM_CHOICE,
        "api_base": os.getenv("OPENAI_API_BASE", "default"),
        "model_name": os.getenv("OPENAI_MODEL_NAME", "default"),
    }
