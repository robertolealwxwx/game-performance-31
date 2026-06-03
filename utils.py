import time

class PerformanceTimer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def duration(self):
        return self.end_time - self.start_time

    def log_duration(self):
        duration = self.duration()
        print(f"Performance duration: {duration:.4f} seconds")


def optimized_function(data):
    # Use a set for O(1) average time complexity
    unique_data = set(data)
    return list(unique_data)  


def process_data(data):
    timer = PerformanceTimer()
    timer.start()
    result = optimized_function(data)
    timer.stop()
    timer.log_duration()
    return result
