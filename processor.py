import requests
import time

class NetworkError(Exception):
    pass

def fetch_data(url, retries=3, backoff=1):
    """Fetches data from a given URL with retry logic."""
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Returning JSON response
        except requests.exceptions.RequestException as e:
            print(f'Attempt {attempt + 1} failed: {e}')  # Log the error
            if attempt < retries - 1:
                time.sleep(backoff * (2 ** attempt))  # Exponential backoff
            else:
                raise NetworkError(f'Failed to fetch data after {retries} attempts')

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = fetch_data(url)
        print(data)
    except NetworkError as ne:
        print(ne)  # Exception handling for network errors