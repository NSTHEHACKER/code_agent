# tests/test_code_generation_agent.py

import unittest
from agents.code_generation_agent import CodeGenerationAgent

class TestCodeGenerationAgent(unittest.TestCase):
    def setUp(self):
        self.agent = CodeGenerationAgent()

    def test_generate_code(self):
        prompt = "Write a Python function to add two numbers."
        code = self.agent.execute_task(prompt)
        self.assertIn("def", code)

if __name__ == '__main__':
    unittest.main()