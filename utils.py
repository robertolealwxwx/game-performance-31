from typing import List, Dict, Any


def calculate_average_score(scores: List[float]) -> float:
    """Calculate the average score from a list of scores.

    Args:
        scores (List[float]): A list of score values.

    Returns:
        float: The average score, or 0 if the list is empty.
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def filter_high_scores(scores: List[float], threshold: float) -> List[float]:
    """Filter and return scores above a given threshold.

    Args:
        scores (List[float]): A list of score values.
        threshold (float): The score threshold.

    Returns:
        List[float]: A list of scores above the threshold.
    """
    return [score for score in scores if score > threshold]


def format_score_info(player_name: str, scores: List[float]) -> Dict[str, Any]:
    """Format player score information as a dictionary.

    Args:
        player_name (str): The name of the player.
        scores (List[float]): A list of score values.

    Returns:
        Dict[str, Any]: A dictionary containing player name and their scores.
    """
    return {
        'player': player_name,
        'average_score': calculate_average_score(scores),
        'high_scores': filter_high_scores(scores, 75.0)
    }  
