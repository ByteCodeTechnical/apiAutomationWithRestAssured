from requests import Session
from utils.logger import get_logger

logger = get_logger(__name__)

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = Session()

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        logger.info(f"Sending GET request to {url} with params: {params}")
        response = self.session.get(url, params=params)
        self._log_response(response)
        return response

    def post(self, endpoint, json=None):
        url = f"{self.base_url}/{endpoint}"
        logger.info(f"Sending POST request to {url} with json: {json}")
        response = self.session.post(url, json=json)
        self._log_response(response)
        return response

    def put(self, endpoint, json=None):
        url = f"{self.base_url}/{endpoint}"
        logger.info(f"Sending PUT request to {url} with json: {json}")
        response = self.session.put(url, json=json)
        self._log_response(response)
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        logger.info(f"Sending DELETE request to {url}")
        response = self.session.delete(url)
        self._log_response(response)
        return response

    def _log_response(self, response):
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.text}")