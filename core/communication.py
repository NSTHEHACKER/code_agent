# core/communication.py

import requests
from utils.logger import Logger

class Communication:
    def __init__(self):
        self.logger = Logger()

    def send_request(self, url: str, data: dict) -> dict:
        """Send a POST request to the given URL with the provided data."""
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            self.logger.info(f"Request sent to {url}: {data}")
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Communication error: {e}")
            return {}