SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
PLAYER_SPEED = 5
ENEMY_SPEED = 3
PROJECTILE_SPEED = 10
BACKGROUND_COLOR = (0, 0, 0)
PLAYER_COLOR = (255, 255, 255)
ENEMY_COLOR = (255, 0, 0)
PROJECTILE_COLOR = (0, 255, 0)
FONT_NAME = 'arial'
FONT_SIZE = 24

COLLISION_MARGIN = 5

LEVELS = {
    1: {'enemy_count': 5, 'difficulty': 'easy'},
    2: {'enemy_count': 10, 'difficulty': 'medium'},
    3: {'enemy_count': 15, 'difficulty': 'hard'},
}

POWER_UPS = {
    'health': {'value': 20, 'duration': 0},
    'speed': {'value': 2, 'duration': 10},
    'damage': {'value': 5, 'duration': 15},
}

ANIMATIONS = {
    'explosion': {'frames': 16, 'duration': 0.5},
    'power_up': {'frames': 8, 'duration': 2},
}

