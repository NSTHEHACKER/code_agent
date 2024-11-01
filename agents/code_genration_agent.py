# agents/code_generation_agent.py

from .agent_base import AgentBase
from core.llm_interface import LLMInterface
from models.model_manager import ModelManager

class CodeGenerationAgent(AgentBase):
    def __init__(self):
        self.model_manager = ModelManager()
        self.llm: LLMInterface = self.model_manager.get_model('ollama')

    def execute_task(self, prompt: str) -> str:
        """Generate code based on the given prompt."""
        return self.llm.generate_code(prompt)