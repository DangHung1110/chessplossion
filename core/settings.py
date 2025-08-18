#screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# Game grid
TILE_SIZE = 32
GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE  # 25 tiles
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE  # 18 tiles

# Player settings
PLAYER_SPEED = 2
PLAYER_SIZE = 24

# Bomb settings
BOMB_TIMER = 3000  # 3 seconds in milliseconds
EXPLOSION_RANGE = 2  # tiles
EXPLOSION_DURATION = 500  # milliseconds
