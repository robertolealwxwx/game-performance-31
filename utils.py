import time
import requests
import random

class NetworkError(Exception):
    pass

def retry_network_operation(func, max_retries=3, delay=2, backoff=2):
    attempts = 0
    while attempts < max_retries:
        try:
            return func()
        except Exception as e:
            attempts += 1
            if attempts == max_retries:
                raise NetworkError(f'Failed after {max_retries} attempts: {str(e)}')
            print(f'Retry {attempts}/{max_retries}...')
            time.sleep(delay)
            delay *= backoff

# Example network operation

def fetch_data():
    if random.choice([True, False]):  # Simulate random failure
        raise Exception('Network failure!')
    return requests.get('https://api.example.com/data').json()

if __name__ == '__main__':
    try:
        data = retry_network_operation(fetch_data)
        print('Data fetched successfully:', data)
    except NetworkError as e:
        print(e)