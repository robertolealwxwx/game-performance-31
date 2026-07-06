from typing import Final

# Constants used throughout the game

# Screen dimensions
SCREEN_WIDTH: Final[int] = 800
SCREEN_HEIGHT: Final[int] = 600

# Frame rate
FPS: Final[int] = 60

# Colors
BLACK: Final[tuple[int, int, int]] = (0, 0, 0)
WHITE: Final[tuple[int, int, int]] = (255, 255, 255)
RED: Final[tuple[int, int, int]] = (255, 0, 0)
GREEN: Final[tuple[int, int, int]] = (0, 255, 0)
BLUE: Final[tuple[int, int, int]] = (0, 0, 255)

# Game states
class GameState:
    MAIN_MENU: Final[str] = 'main_menu'
    PLAYING: Final[str] = 'playing'
    PAUSED: Final[str] = 'paused'
    GAME_OVER: Final[str] = 'game_over'

# Default settings
DEFAULT_VOLUME: Final[float] = 0.5
DEFAULT_DIFFICULTY: Final[str] = 'normal'

