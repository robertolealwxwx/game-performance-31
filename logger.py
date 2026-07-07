import logging
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, name, log_file, max_bytes=5*1024*1024, backup_count=5):
        """Initialize logger with rotating file handler."""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

# Example usage:
if __name__ == '__main__':
    app_logger = Logger('MyApp', 'app.log')
    app_logger.info('Logger has been set up successfully.')