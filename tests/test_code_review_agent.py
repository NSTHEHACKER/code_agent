# tests/test_code_review_agent.py

import unittest
from agents.code_review_agent import CodeReviewAgent

class TestCodeReviewAgent(unittest.TestCase):
    def setUp(self):
        self.agent = CodeReviewAgent()

    def test_review_code(self):
        code = "def add(a, b):\n    return a + b"
        feedback = self.agent.execute_task(code)
        self.assertIn("good", feedback.lower())

if __name__ == '__main__':
    unittest.main()