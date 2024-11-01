# core/task_manager.py

from agents.agent_manager import AgentManager
from utils.logger import Logger

class TaskManager:
    def __init__(self):
        self.agent_manager = AgentManager()
        self.logger = Logger()

    def run_task_sequence(self, prompt: str):
        """Run the sequence: Generate -> Review -> Test -> Deploy."""
        self.logger.info("Starting task sequence.")

        # Generate Code
        generated_code = self.agent_manager.execute_agent('code_generation', prompt)
        self.logger.info("Code generation completed.")

        # Review Code
        review_feedback = self.agent_manager.execute_agent('code_review', generated_code)
        self.logger.info("Code review completed.")

        # Save generated code to a file
        file_manager = FileManager()
        file_manager.write_file('generated_code.py', generated_code)

        # Run Tests
        test_results = self.agent_manager.execute_agent('testing', 'pytest')
        self.logger.info("Testing completed.")

        if "FAILED" not in test_results:
            # Deploy Code
            deployment_output = self.agent_manager.execute_agent('deployment', './deploy.sh')
            self.logger.info("Deployment completed.")
            return deployment_output
        else:
            self.logger.error("Tests failed. Deployment aborted.")
            return "Deployment aborted due to test failures."