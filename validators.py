def validate_user_input(user_input):
    """
    Validate the input from the user.
    Checks if the input is a non-empty string.
    """
    if not isinstance(user_input, str):
        raise ValueError("Input must be a string.")
    if user_input.strip() == '':
        raise ValueError("Input cannot be empty or just whitespace.")
    return True

def validate_game_choice(choice, valid_choices):
    """
    Validate the user's game choice.
    Checks if the choice is in the list of valid choices.
    """
    if choice not in valid_choices:
        raise ValueError(f"Invalid choice: {choice}. Choose from {valid_choices}.")
    return True

# Example main processing loop using input validation
if __name__ == '__main__':
    valid_games = ['Game1', 'Game2', 'Game3']
    while True:
        user_input = input("Enter game choice: ")
        try:
            validate_user_input(user_input)
            validate_game_choice(user_input, valid_games)
            print(f"You selected: {user_input}")
            break  # Exit loop on valid input
        except ValueError as e:
            print(e)  # Inform user about the error