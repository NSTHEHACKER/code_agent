# models/model_manager.py

from .app_model import AppModel
from .ollama_model import OllamaModel
from core.config import Config

class ModelManager:
    def __init__(self):
        self.models = {
            'ollama': OllamaModel(name='Ollama', api_key=Config.OLLAMA_API_KEY),
            # Add other models like 'mistal', 'groq' as needed
        }

    def get_model(self, model_name: str):
        return self.models.get(model_name)