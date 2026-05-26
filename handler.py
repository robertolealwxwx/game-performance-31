import sys
import re

# Function to validate user input

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError("Input must be a string.")
    if len(user_input) == 0:
        raise ValueError("Input cannot be empty.")
    if not re.match("^[A-Za-z0-9_]*$, user_input):
        raise ValueError("Input can only contain alphanumeric characters and underscores.")

# Main processing loop

def main_loop():
    while True:
        try:
            user_input = input("Enter command: ")
            validate_input(user_input)
            print(f"You entered a valid command: {user_input}")
            # Here you can include the logic to handle valid commands
        except ValueError as e:
            print(f"Error: {e}")  
        except KeyboardInterrupt:
            print("Exiting the game.")
            sys.exit(0)

if __name__ == '__main__':
    main_loop()