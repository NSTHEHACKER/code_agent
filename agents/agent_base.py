# agents/agent_base.py

from abc import ABC, abstractmethod

class AgentBase(ABC):
    @abstractmethod
    def execute_task(self, task):
        """Execute a given task."""
        pass