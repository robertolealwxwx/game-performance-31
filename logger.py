import logging
from logging.handlers import RotatingFileHandler

# Logger configuration

def setup_logger(log_file='game.log', max_bytes=5*1024*1024, backup_count=3):
    logger = logging.getLogger('GameLogger')
    logger.setLevel(logging.DEBUG)

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)

    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    my_logger = setup_logger()
    my_logger.info('Logger is set up and ready')
    my_logger.error('This is an error message')
    my_logger.debug('Debugging information here')