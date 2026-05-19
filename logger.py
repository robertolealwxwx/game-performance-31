import logging

# Configure the logger for performance tracking
class PerformanceLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        handler = logging.FileHandler('performance.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log_event(self, event_name, duration):
        self.logger.info(f'Event: {event_name}, Duration: {duration:.6f} seconds')

    def log_error(self, error_message):
        self.logger.error(f'Error: {error_message}')