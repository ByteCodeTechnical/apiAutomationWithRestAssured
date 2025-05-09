from utils.logger import setup_logger
import pytest

@pytest.fixture(scope='session', autouse=True)
def setup():
    setup_logger()  # Initialize the logger for the test session
    yield  # This will allow the tests to run
    # Any teardown code can be added here if needed