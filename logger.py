import logging

# Configure the logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_input_validation(input_data):
    # Log the input being validated
    logger.debug(f'Validating input: {input_data}')

def log_validation_result(is_valid):
    # Log the result of validation
    if is_valid:
        logger.info('Input is valid.')
    else:
        logger.warning('Input is invalid.')

if __name__ == '__main__':
    # Example usage of the logger
    test_input = 'example_input'
    log_input_validation(test_input)
    log_validation_result(True)