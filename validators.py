import re

def is_valid_username(username):
    """
    Validate the username based on specific criteria:
    - Must be alphanumeric
    - Should be between 3 to 20 characters
    """
    if not (3 <= len(username) <= 20):
        return False
    return username.isalnum()

def is_valid_email(email):
    """
    Validate the email format using regex.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def is_valid_password(password):
    """
    Validate the password based on specific criteria:
    - Must be at least 8 characters
    - Must contain at least one uppercase letter
    - Must contain at least one number
    """
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_upper and has_digit

if __name__ == '__main__':
    # Example usage:
    print(is_valid_username('Player1'))  # True
    print(is_valid_email('player@example.com'))  # True
    print(is_valid_password('Password1'))  # True
