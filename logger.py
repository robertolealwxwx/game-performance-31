import logging

# Configure the logger for the game
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('game.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()

# Function to log game events

def log_event(event_type, message):
    """
    Logs an event message with a specific type.

    :param event_type: Type of the event (e.g., INFO, WARNING, ERROR)
    :param message: Message to log
    """
    if event_type == 'info':
        logger.info(message)
    elif event_type == 'warning':
        logger.warning(message)
    elif event_type == 'error':
        logger.error(message)
    elif event_type == 'debug':
        logger.debug(message)
    else:
        logger.error('Unknown event type: %s', event_type)

# Example usage
if __name__ == '__main__':
    log_event('info', 'Game started')
    log_event('debug', 'Loading resources')
    log_event('warning', 'Low memory warning')
    log_event('error', 'Failed to load level')