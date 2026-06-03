import logging
from logging.handlers import RotatingFileHandler

# Set up a logger for the application
logger = logging.getLogger('game_logger')
logger.setLevel(logging.DEBUG)  # Set the minimum logging level

# Create a rotating file handler that logs to 'app.log'
handler = RotatingFileHandler('app.log', maxBytes=5*1024*1024, backupCount=3)  # 5MB size limit
handler.setLevel(logging.DEBUG)  # Set the level for the handler

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Example usage
logger.info('Logger setup complete.')  # Log an info message
logger.warning('This is a warning message.')  # Log a warning message
logger.error('This is an error message.')  # Log an error message
