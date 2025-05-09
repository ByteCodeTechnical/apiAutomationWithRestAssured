from allure_commons.types import AttachmentType
import allure
import logging

logger = logging.getLogger(__name__)

def attach_log_to_allure(log_message):
    logger.info(log_message)
    allure.attach(log_message, name="Log", attachment_type=AttachmentType.TEXT) 

def attach_result_to_allure(result):
    allure.attach(str(result), name="Result", attachment_type=AttachmentType.TEXT) 

def attach_exception_to_allure(exception):
    logger.error(f"Exception occurred: {exception}")
    allure.attach(str(exception), name="Exception", attachment_type=AttachmentType.TEXT)