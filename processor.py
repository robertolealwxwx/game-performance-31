import time

class GameProcessor:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start_timer(self):
        """Start the timing for game execution."""
        self.start_time = time.time()
        print("Timer started.")

    def stop_timer(self):
        """Stop the timing and return the elapsed time."""
        if self.start_time is None:
            raise Exception("Timer was not started.\n")
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Timer stopped. Elapsed time: {elapsed_time:.2f} seconds")
        return elapsed_time

    def reset_timer(self):
        """Reset the timer to initial state."""
        self.start_time = None
        self.end_time = None
        print("Timer reset.")

    def process_game_data(self, data):
        """Simulate processing of game data."""
        print(f"Processing game data: {data}")
        time.sleep(0.3)  # Simulating processing time

    def run(self, data):
        """Run the game processor with the provided data."""
        self.start_timer()
        self.process_game_data(data)
        self.stop_timer()
