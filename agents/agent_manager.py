# agents/agent_manager.py

from .agent_base import AgentBase
from .code_generation_agent import CodeGenerationAgent
from .code_review_agent import CodeReviewAgent
from .deployment_agent import DeploymentAgent
from .testing_agent import TestingAgent

class AgentManager:
    def __init__(self):
        self.agents = {
            'code_generation': CodeGenerationAgent(),
            'code_review': CodeReviewAgent(),
            'deployment': DeploymentAgent(),
            'testing': TestingAgent()
        }

    def get_agent(self, agent_type: str) -> AgentBase:
        return self.agents.get(agent_type)
    
    def execute_agent(self, agent_type: str, task):
        agent = self.get_agent(agent_type)
        if agent:
            return agent.execute_task(task)
        else:
            raise ValueError(f"Agent type '{agent_type}' not found.")