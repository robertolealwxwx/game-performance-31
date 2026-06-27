from typing import List, Dict


def calculate_average(scores: List[float]) -> float:
    """
    Calculate the average of a list of scores.

    Args:
        scores (List[float]): A list of float scores.

    Returns:
        float: The average score calculated as a float.
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def find_high_score(scores: List[float]) -> float:
    """
    Find the highest score from a list of scores.

    Args:
        scores (List[float]): A list of float scores.

    Returns:
        float: The highest score found.
    """
    if not scores:
        return 0.0
    return max(scores)


def score_summary(scores: List[float]) -> Dict[str, float]:
    """
    Generate a summary of scores including average and high score.

    Args:
        scores (List[float]): A list of float scores.

    Returns:
        Dict[str, float]: A dictionary containing average and high score.
    """
    return {
        'average': calculate_average(scores),
        'high_score': find_high_score(scores)
    }