import sys
import json

class InvalidInputError(Exception):
    pass

def validate_user_input(user_input):
    if not isinstance(user_input, dict):
        raise InvalidInputError('Input must be a dictionary.')
    if 'action' not in user_input:
        raise InvalidInputError('Input must contain an action key.')
    if user_input['action'] not in ['start', 'stop', 'pause']:
        raise InvalidInputError('Invalid action specified.')

def main_processing_loop():
    while True:
        user_input = input('Enter command (in JSON format): ')
        try:
            user_input = json.loads(user_input)
            validate_user_input(user_input)
            process_command(user_input)
        except json.JSONDecodeError:
            print('Invalid JSON format, please try again.')
        except InvalidInputError as e:
            print(f'Input validation error: {e}')
        except KeyboardInterrupt:
            print('\nExiting the program. Thank you!')
            sys.exit(0)

def process_command(user_input):
    action = user_input['action']
    if action == 'start':
        print('Game started!')
    elif action == 'stop':
        print('Game stopped!')
    elif action == 'pause':
        print('Game paused!')

if __name__ == '__main__':
    print('Starting main processing loop...')
    main_processing_loop()