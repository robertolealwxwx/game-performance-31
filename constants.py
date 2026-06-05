from typing import Tuple

# Constants for game configuration
FPS: int = 60  # Frames per second

# Game resolution
SCREEN_WIDTH: int = 1280
SCREEN_HEIGHT: int = 720

# Colors represented in RGB
BLACK: Tuple[int, int, int] = (0, 0, 0)
WHITE: Tuple[int, int, int] = (255, 255, 255)
RED: Tuple[int, int, int] = (255, 0, 0)
GREEN: Tuple[int, int, int] = (0, 255, 0)
BLUE: Tuple[int, int, int] = (0, 0, 255)

def get_game_resolution() -> Tuple[int, int]:
    """Return the game resolution as a tuple of (width, height)."""
    return SCREEN_WIDTH, SCREEN_HEIGHT

def get_fps() -> int:
    """Return the frames per second for the game."""
    return FPS
