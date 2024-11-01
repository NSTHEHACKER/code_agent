# tests/test_task_manager.py

import unittest
from core.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    def test_run_task_sequence(self):
        prompt = "Write a Python class for a binary search tree."
        result = self.task_manager.run_task_sequence(prompt)
        self.assertIn("Deployment", result)

if __name__ == '__main__':
    unittest.main()