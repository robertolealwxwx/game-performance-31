import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, backoff_factor=0.3):
    """
    Makes a network request with retry logic.
    :param url: URL to perform the request
    :param retries: Number of times to retry
    :param backoff_factor: Factor for exponential backoff
    :return: Response object
    """
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            if attempt < retries - 1:
                wait_time = backoff_factor * (2 ** attempt)
                time.sleep(wait_time)
            else:
                raise NetworkError(f'Failed to fetch {url}: {str(e)}')
