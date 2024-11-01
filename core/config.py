# core/config.py

import os

class Config:
    """Configuration settings for the application."""
    OLLAMA_API_KEY = os.getenv('OLLAMA_API_KEY')
    MISTAL_API_KEY = os.getenv('MISTAL_API_KEY')
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    DEPLOYMENT_SCRIPT = os.getenv('DEPLOYMENT_SCRIPT', './deploy.sh')
    TEST_COMMAND = os.getenv('TEST_COMMAND', 'pytest')