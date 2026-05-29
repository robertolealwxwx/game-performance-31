from typing import Final

# Game-related constants

# Screen dimensions
SCREEN_WIDTH: Final[int] = 1024
SCREEN_HEIGHT: Final[int] = 768

# Frame rate settings
FPS: Final[int] = 60

# Color constants (RGB)
BLACK: Final[tuple[int, int, int]] = (0, 0, 0)
WHITE: Final[tuple[int, int, int]] = (255, 255, 255)
RED: Final[tuple[int, int, int]] = (255, 0, 0)
GREEN: Final[tuple[int, int, int]] = (0, 255, 0)
BLUE: Final[tuple[int, int, int]] = (0, 0, 255)

# Minimum and maximum player health
MIN_HEALTH: Final[int] = 0
MAX_HEALTH: Final[int] = 100

# Game levels
LEVELS: Final[list[str]] = ["Easy", "Medium", "Hard"]

# Difficulty multipliers
DIFFICULTY_MULTIPLIERS: Final[dict[str, float]] = {
    "Easy": 1.0,
    "Medium": 1.5,
    "Hard": 2.0,
}

# Game keys
MOVE_UP: Final[str] = 'w'
MOVE_DOWN: Final[str] = 's'
MOVE_LEFT: Final[str] = 'a'
MOVE_RIGHT: Final[str] = 'd'
