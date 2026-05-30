import logging
from logging.handlers import RotatingFileHandler

# Set up logger configuration
def setup_logger(logger_name, log_file, level=logging.INFO):
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)  # 5 MB
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    my_logger = setup_logger('game_logger', 'game_performance.log')
    my_logger.info('Game logger started. All systems go!')
    my_logger.error('This is an error message for testing.')
