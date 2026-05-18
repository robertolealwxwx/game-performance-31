def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    if len(user_input) > 100:
        raise ValueError('Input exceeds maximum length of 100 characters')
    return user_input

if __name__ == '__main__':
    try:
        user_input = input('Enter your command: ')
        valid_input = validate_input(user_input)
        print(f'Valid input received: {valid_input}')
    except ValueError as e:
        print(f'Input validation error: {e}')