# models/ollama_model.py

from core.llm_interface import LLMInterface
import requests
from core.config import Config

class OllamaModel(LLMInterface):
    def __init__(self, name: str, api_key: str):
        self.name = name
        self.api_key = api_key
        self.endpoint = "https://api.ollama.com/generate"

    def generate_code(self, prompt: str) -> str:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"prompt": prompt}
        response = requests.post(self.endpoint, headers=headers, json=data)
        if response.status_code == 200:
            return response.json().get('code', '')
        else:
            return "Error generating code."

    def review_code(self, code: str) -> str:
        # Implement review functionality or use a different endpoint
        review_endpoint = "https://api.ollama.com/review"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"code": code}
        response = requests.post(review_endpoint, headers=headers, json=data)
        if response.status_code == 200:
            return response.json().get('feedback', '')
        else:
            return "Error reviewing code."