from typing import Optional


def is_valid_score(score: int) -> bool:
    """
    Validates if the provided score is within acceptable limits.

    Args:
        score (int): The score to validate.

    Returns:
        bool: True if the score is valid, False otherwise.
    """
    return 0 <= score <= 100


def is_valid_username(username: str) -> bool:
    """
    Validates if the username meets required criteria.

    Args:
        username (str): The username to validate.

    Returns:
        bool: True if the username is valid, False otherwise.
    """
    return len(username) >= 3 and len(username) <= 20 and username.isalnum()


def is_valid_email(email: str) -> bool:
    """
    Validates the format of an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email format is valid, False otherwise.
    """
    import re
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.match(email_regex, email) is not None


def is_valid_password(password: str) -> bool:
    """
    Validates the strength of a password.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is strong, False otherwise.
    """
    return len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password)