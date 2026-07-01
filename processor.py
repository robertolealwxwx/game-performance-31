import time
import random

class GameProcessor:
    def __init__(self):
        self.players = []
        self.performance_metrics = []

    def add_player(self, player_id):
        self.players.append(player_id)

    def optimize_player_actions(self):
        # Optimize actions with simple sampling to reduce load
        sampled_players = random.sample(self.players, min(3, len(self.players)))
        for player in sampled_players:
            self.perform_actions(player)

    def perform_actions(self, player):
        # Simulating action performance with time tracking
        start_time = time.time()
        action_time = random.uniform(0.1, 0.5)
        time.sleep(action_time)  # Simulate action duration
        end_time = time.time()

        # Store performance metrics
        self.performance_metrics.append({'player': player, 'action_time': end_time - start_time})

    def get_performance_metrics(self):
        return self.performance_metrics

if __name__ == '__main__':
    processor = GameProcessor()
    # Add players to the game
    for i in range(10):
        processor.add_player(f'player_{i}')
    
    # Optimize actions and capture performance
o = processor.optimize_player_actions()
    print(processor.get_performance_metrics())