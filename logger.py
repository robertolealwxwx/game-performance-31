import logging
from logging.handlers import RotatingFileHandler

# Configure logger
logger = logging.getLogger('game_logger')
logger.setLevel(logging.DEBUG)

# Create a file handler that logs debug and higher level messages
handler = RotatingFileHandler('game_performance.log', maxBytes=5 * 1024 * 1024, backupCount=3)
handler.setLevel(logging.DEBUG)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Simple log record for testing
if __name__ == '__main__':
    logger.info('Logger is set up and ready to go!')