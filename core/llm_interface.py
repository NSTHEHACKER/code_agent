# core/llm_interface.py

from abc import ABC, abstractmethod

class LLMInterface(ABC):
    @abstractmethod
    def generate_code(self, prompt: str) -> str:
        pass

    @abstractmethod
    def review_code(self, code: str) -> str:
        pass