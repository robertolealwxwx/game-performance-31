import logging
from logging.handlers import RotatingFileHandler

# Set up the logger
logger = logging.getLogger('game_performance_logger')
logger.setLevel(logging.DEBUG)

# Create a rotating file handler
handler = RotatingFileHandler('game_performance.log', maxBytes=5*1024*1024, backupCount=3)
handler.setLevel(logging.DEBUG)

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Example usage of the logger
if __name__ == '__main__':
    logger.info('Logger setup complete.')
    logger.debug('This is a debug message.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
    logger.critical('This is a critical message.')
