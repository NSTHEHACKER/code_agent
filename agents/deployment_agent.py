# agents/deployment_agent.py

from .agent_base import AgentBase
import subprocess
from utils.logger import Logger

class DeploymentAgent(AgentBase):
    def __init__(self):
        self.logger = Logger()

    def execute_task(self, deployment_script: str) -> str:
        """Deploy code using the provided deployment script."""
        try:
            result = subprocess.run(deployment_script, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.logger.info(f"Deployment successful: {result.stdout.decode()}")
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Deployment failed: {e.stderr.decode()}")
            return e.stderr.decode()