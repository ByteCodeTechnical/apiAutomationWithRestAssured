from src.api.client import APIClient
from src.utils.logger import get_logger
import pytest

logger = get_logger(__name__)

@pytest.fixture(scope="module")
def api_client():
    client = APIClient(base_url="http://localhost:8000")  # Replace with actual base URL
    yield client

def test_example_endpoint(api_client):
    logger.info("Starting test for example endpoint")
    response = api_client.get("/example")
    logger.info(f"Response received: {response.status_code} - {response.json()}")
    
    assert response.status_code == 200
    assert "data" in response.json()  # Adjust based on actual response structure

def test_example_endpoint_post(api_client):
    logger.info("Starting POST test for example endpoint")
    payload = {"key": "value"}
    response = api_client.post("/example", json=payload)
    logger.info(f"Response received: {response.status_code} - {response.json()}")
    
    assert response.status_code == 201
    assert response.json().get("key") == "value"  # Adjust based on actual response structure