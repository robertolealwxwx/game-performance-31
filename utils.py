import numpy as np
import random


def calculate_average(scores):
    """Calculate the average of a list of scores."""
    if not scores:
        return 0
    return sum(scores) / len(scores)


def find_high_score(scores):
    """Return the highest score from a list."""
    if not scores:
        return None
    return max(scores)


def generate_random_item(items):
    """Select a random item from a list."""
    if not items:
        return None
    return random.choice(items)


def normalize_scores(scores):
    """Normalize a list of scores to a range of 0 to 1."""
    if not scores:
        return []
    max_score = max(scores)
    return [score / max_score for score in scores]


def shuffle_list(lst):
    """Shuffle a list in place and return it."""
    random.shuffle(lst)
    return lst


# Example Usage:
# scores = [10, 20, 30]
# print(calculate_average(scores))
# print(find_high_score(scores))
# items = ['sword', 'shield', 'potion']
# print(generate_random_item(items))
# print(normalize_scores(scores))
# print(shuffle_list(items))
