import logging
from logging.handlers import RotatingFileHandler

# Set up basic configuration for logging
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_FILE = 'game_performance.log'
LOG_MAX_BYTES = 5 * 1024 * 1024  # 5 MB
LOG_BACKUP_COUNT = 3

def setup_logger():
    
    logger = logging.getLogger('game_performance_logger')
    logger.setLevel(logging.DEBUG)
    
    # Create a rotating file handler
    handler = RotatingFileHandler(LOG_FILE, maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT)
    handler.setFormatter(logging.Formatter(LOG_FORMAT))
    
    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example usage
debug_logger = setup_logger()
debug_logger.info('Logger is set up successfully.')