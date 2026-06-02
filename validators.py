def is_valid_username(username):
    """
    Validate username for length and characters.
    Username must be 3-15 characters long and can include letters, numbers, and underscores.
    """
    if not (3 <= len(username) <= 15):
        return False
    if not username.isalnum() and '_' not in username:
        return False
    return True


def is_valid_password(password):
    """
    Validate password strength.
    Password must be at least 8 characters long, contain at least one digit,
    one uppercase letter, and one special character.
    """
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()-+=' for char in password):
        return False
    return True


def is_valid_email(email):
    """
    Validate email format using a simple regex pattern.
    """
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


if __name__ == '__main__':
    # Test the validation functions
    print(is_valid_username('user_name123'))  # True
    print(is_valid_password('StrongP@ss1'))   # True
    print(is_valid_email('email@example.com'))  # True
