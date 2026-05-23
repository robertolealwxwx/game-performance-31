import re

class ValidationError(Exception):
    pass

def validate_username(username):
    if not isinstance(username, str):
        raise ValidationError('Username must be a string.')
    if len(username) < 3 or len(username) > 20:
        raise ValidationError('Username must be between 3 to 20 characters.')
    if not re.match('^[a-zA-Z0-9_]*$', username):
        raise ValidationError('Username can only contain letters, numbers, and underscores.')

def validate_email(email):
    if not isinstance(email, str):
        raise ValidationError('Email must be a string.')
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise ValidationError('Invalid email format.')

def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError('Age must be an integer.')
    if age < 0 or age > 120:
        raise ValidationError('Age must be between 0 and 120.')

if __name__ == '__main__':
    # Sample validations for testing
    try:
        validate_username('user_1')
        validate_email('example@test.com')
        validate_age(25)
        print('All validations passed!')
    except ValidationError as e:
        print(f'Validation error: {e}')