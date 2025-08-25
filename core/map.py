import pygame
from core.settings import *
from core.constants import *

class GameMap:
    def __init__(self):
        self.grid = self.create_map()
        self.tile_size = TILE_SIZE

    def create_map(self):
        import random
        grid = []

        for y in range(GRID_HEIGHT):
            row = []
            for x in range(GRID_WIDTH):
                # Tường viền
                if x == 0 or x == GRID_WIDTH - 1 or y == 0 or y == GRID_HEIGHT - 1:
                    row.append(WALL)
                # Cột tường cố định ở các vị trí chẵn-chẵn (Bomberman/Chessplosion-style)
                elif x % 2 == 0 and y % 2 == 0:
                    row.append(WALL)
                else:
                    # Mặc định rỗng, lát nữa sẽ rải tường phá được
                    row.append(EMPTY)
            grid.append(row)

        # Vùng spawn an toàn cho 2 góc đối diện (mỗi vùng 3x3, clear lối ra)
        def clear_spawn_area(cx, cy):
            safe_coords = [
                (cx, cy), (cx + 1, cy), (cx, cy + 1)
            ]
            for sx, sy in safe_coords:
                if 0 <= sx < GRID_WIDTH and 0 <= sy < GRID_HEIGHT and grid[sy][sx] != WALL:
                    grid[sy][sx] = EMPTY

        # Spawn 1: (1,1). Spawn 2: (GRID_WIDTH-2, GRID_HEIGHT-2)
        clear_spawn_area(1, 1)
        clear_spawn_area(GRID_WIDTH - 2, GRID_HEIGHT - 2)

        # Rải tường phá được (không đặt vào tường cứng hay vùng spawn)
        for y in range(1, GRID_HEIGHT - 1):
            for x in range(1, GRID_WIDTH - 1):
                if grid[y][x] == EMPTY:
                    # Tránh 2 vùng spawn mở rộng 2x2
                    in_spawn1 = (x <= 2 and y <= 2)
                    in_spawn2 = (x >= GRID_WIDTH - 3 and y >= GRID_HEIGHT - 3)
                    if not in_spawn1 and not in_spawn2:
                        if random.random() < 0.35:
                            grid[y][x] = DESTRUCTIBLE_WALL

        # Debug
        print(f"Map created: {GRID_WIDTH}x{GRID_HEIGHT}")
        print(f"Player1 spawn (1,1): {grid[1][1]} (0=EMPTY, 1=WALL, 2=DESTRUCTIBLE)")
        print(
            f"Player2 spawn ({GRID_WIDTH-2},{GRID_HEIGHT-2}): {grid[GRID_HEIGHT-2][GRID_WIDTH-2]}"
        )

        return grid
    
    def get_tile(self, x, y):
        # Lấy tile tại vị trí (x, y)
        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            return self.grid[y][x]
        return WALL  # Ngoài map coi như tường
    
    def set_tile(self, x, y, tile_type):
        # Set tile tại vị trí (x, y)
        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            self.grid[y][x] = tile_type
    
    def is_walkable(self, x, y):
        # Check xem tile có đi được không
        tile = self.get_tile(x, y)
        return tile == EMPTY
    
    def draw(self, screen):
        # Vẽ map lên screen 
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                tile = self.grid[y][x]
                rect = pygame.Rect(
                    x * self.tile_size, 
                    y * self.tile_size, 
                    self.tile_size, 
                    self.tile_size
                )
                
                # Vẽ tile theo loại
                if tile == WALL:
                    pygame.draw.rect(screen, GRAY, rect)
                elif tile == DESTRUCTIBLE_WALL:
                    pygame.draw.rect(screen, (139, 69, 19), rect)  # Brown
                else:
                    pygame.draw.rect(screen, BLACK, rect)
                
                # Vẽ border
                pygame.draw.rect(screen, WHITE, rect, 1)
