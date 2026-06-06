import logging
from logging.handlers import RotatingFileHandler

# Function to set up logger with rotation

def setup_logger(log_file='game_performance.log', max_bytes=1e6, backup_count=5):
    """
    Sets up a logger with a rotating file handler.
    :param log_file: The name of the log file.
    :param max_bytes: Maximum file size before rotation (in bytes).
    :param backup_count: Number of backup log files to keep.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger is set up and ready to go.')