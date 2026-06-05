import logging
from logging.handlers import RotatingFileHandler


def setup_logger(log_file, max_bytes=5*1024*1024, backup_count=3):
    """Sets up a rotating logger that records game performance logs."""
    logger = logging.getLogger("GamePerformanceLogger")
    logger.setLevel(logging.DEBUG)

    # Create a file handler that rotates logs
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    if not logger.hasHandlers():
        logger.addHandler(handler)
    return logger


# Example usage - typically placed in the entry point of your application
if __name__ == "__main__":
    log = setup_logger('game_performance.log')
    log.info('Logger is set up and ready')