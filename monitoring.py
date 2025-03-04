"""
Asynchronous monitoring and structured logging configuration.
This example configures logging in JSON format.
"""

import logging
import json
from pythonjsonlogger import jsonlogger

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(message)s')
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

def log_error(message: str, error: Exception):
    """
    Log an error message with error details using structured JSON logging.
    """
    logger.error(json.dumps({
        "message": message,
        "error": str(error)
    }))