# utils/code_utils.py

import re

class CodeUtils:
    @staticmethod
    def format_code(code: str) -> str:
        """Format code using regex or integrate with a formatter like Black."""
        # Simple example: remove trailing whitespace
        return re.sub(r'[ \t]+$', '', code, flags=re.MULTILINE)
    
    @staticmethod
    def parse_code(code: str) -> list:
        """Parse code into lines or tokens."""
        return code.split('\n')