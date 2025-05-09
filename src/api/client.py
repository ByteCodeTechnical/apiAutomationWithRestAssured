from requests import Session
from utils.logger import get_logger

logger = get_logger(__name__)
    def __init__(self, name):
class APIClient:ger = logging.getLogger(name)
    def __init__(self, base_url):ing.DEBUG)
        self.base_url = base_urlndler(os.path.join(os.getcwd(), 'logs', f'{name}.log'))
        self.session = Session().DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        logger.info(f"Sending GET request to {url} with params: {params}")
        response = self.session.get(url, params=params)
        self._log_response(response)
        return response
    def info(self, message):
    def post(self, endpoint, json=None):
        url = f"{self.base_url}/{endpoint}"
        logger.info(f"Sending POST request to {url} with json: {json}")
        response = self.session.post(url, json=json)
        self._log_response(response)
        return responsesage):
        self.logger.error(message)
    def put(self, endpoint, json=None):
        url = f"{self.base_url}/{endpoint}"
        logger.info(f"Sending PUT request to {url} with json: {json}")
        response = self.session.put(url, json=json)
        self._log_response(response)onse)
        return response
    return Logger(name)        return response
    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        logger.info(f"Sending DELETE request to {url}")
        response = self.session.delete(url)t to {url}")
        self._log_response(response)te(url)
        return responsense(response)
        return response
    def _log_response(self, response):
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.text}")status_code}")
        logger.info(f"Response body: {response.text}")