from typing import List, Dict


def process_game_data(game_data: List[Dict[str, str]]) -> Dict[str, int]:
    """Processes game data to calculate score totals.

    Args:
        game_data (List[Dict[str, str]]): A list of game data dictionaries, each containing 'score' and 'player_name'.

    Returns:
        Dict[str, int]: A dictionary with player names as keys and their total scores as values.
    """
    total_scores: Dict[str, int] = {}
    
    for entry in game_data:
        player_name = entry.get('player_name')
        score = int(entry.get('score', 0))
        if player_name:
            if player_name not in total_scores:
                total_scores[player_name] = 0
            total_scores[player_name] += score
    
    return total_scores
