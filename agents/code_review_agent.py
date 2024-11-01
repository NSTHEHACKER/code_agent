# agents/code_review_agent.py

from .agent_base import AgentBase
from core.llm_interface import LLMInterface
from models.model_manager import ModelManager

class CodeReviewAgent(AgentBase):
    def __init__(self):
        self.model_manager = ModelManager()
        self.llm: LLMInterface = self.model_manager.get_model('mistal')

    def execute_task(self, code: str) -> str:
        """Review and analyze the given code."""
        return self.llm.review_code(code)