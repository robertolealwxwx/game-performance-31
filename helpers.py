import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, backoff=1):
    """Perform a network request with retry logic."""
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON data if successful
        except requests.exceptions.RequestException as e:
            attempt += 1
            if attempt == retries:
                raise NetworkError(f'Failed to fetch data after {retries} attempts') from e
            time.sleep(backoff * (2 ** (attempt - 1)))  # Exponential backoff

# Example usage
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except NetworkError as ne:
        print(ne)