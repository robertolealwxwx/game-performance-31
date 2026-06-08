import logging
from logging.handlers import RotatingFileHandler


def setup_logger(log_file='app.log', max_bytes=5 * 1024 * 1024, backup_count=3):
    """
    Set up a logger that writes to a file with rotation.
    :param log_file: Filename for the log file
    :param max_bytes: Maximum file size before rotation
    :param backup_count: Number of backup files to keep
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


# Example usage
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger is set up.')