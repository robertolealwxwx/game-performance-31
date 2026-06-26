import numpy as np


def calculate_average(frames_per_second_list):
    """
    Calculate the average frames per second.
    
    Args:
        frames_per_second_list (list): A list of FPS values.
    
    Returns:
        float: The average FPS.
    """
    return np.mean(frames_per_second_list)


def filter_low_fps(frames_per_second_list, threshold):
    """
    Filter out FPS values lower than the threshold.
    
    Args:
        frames_per_second_list (list): A list of FPS values.
        threshold (float): The threshold value for filtering.
    
    Returns:
        list: A list of FPS values above the threshold.
    """
    return [fps for fps in frames_per_second_list if fps >= threshold]


def normalize_values(values):
    """
    Normalize a list of values to the range [0, 1].
    
    Args:
        values (list): A list of numerical values.
    
    Returns:
        list: A list of normalized values.
    """
    min_val = min(values)
    max_val = max(values)
    return [(val - min_val) / (max_val - min_val) for val in values]