# agents/testing_agent.py

from .agent_base import AgentBase
from utils.file_manager import FileManager
from utils.logger import Logger
import subprocess

class TestingAgent(AgentBase):
    def __init__(self):
        self.file_manager = FileManager()
        self.logger = Logger()

    def execute_task(self, test_command: str) -> str:
        """Run test cases using the provided test command."""
        try:
            result = subprocess.run(test_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.logger.info(f"Tests passed: {result.stdout.decode()}")
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Tests failed: {e.stderr.decode()}")
            return e.stderr.decode()