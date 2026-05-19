import logging
import os
from logging.handlers import RotatingFileHandler

# Constants for logger configuration
LOG_FILE = 'game_performance.log'
LOG_LEVEL = logging.DEBUG

def setup_logger():
    # Create a logger object
    logger = logging.getLogger('GamePerformanceLogger')
    logger.setLevel(LOG_LEVEL)

    # Create a rotating file handler
    handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=3)
    handler.setLevel(LOG_LEVEL)

    # Create and set formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

# Example usage
if __name__ == '__main__':
    log = setup_logger()
    log.debug('Logger is set up and ready to use!')