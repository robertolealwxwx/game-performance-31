import sys

# Constants for input validation
VALID_INPUTS = {'up', 'down', 'left', 'right', 'quit'}

class Game:
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            user_input = input('Enter your move (up, down, left, right, quit): ')
            self.process_input(user_input)

    def process_input(self, user_input):
        # Validate input
        if self.validate_input(user_input):
            self.handle_move(user_input)
        else:
            print(f'Invalid input: {user_input}. Please try again.')

    def validate_input(self, user_input):
        return user_input in VALID_INPUTS

    def handle_move(self, move):
        if move == 'quit':
            self.running = False
            print('Exiting the game.')
        else:
            print(f'You moved {move}.')

if __name__ == '__main__':
    game = Game()
    game.run()