import pygame
from core.settings import *
from core.constants import *

class GameMap:
    def __init__(self):
        self.grid = self.create_map()
        self.tile_size = TILE_SIZE

    def create_map(self):
        grid = []
        
        for y in range(GRID_HEIGHT):
            row = []
            for x in range(GRID_WIDTH):
                # Tường viền
                if x == 0 or x == GRID_WIDTH-1 or y == 0 or y == GRID_HEIGHT-1:
                    row.append(WALL)
                # Tường cột chẵn/hàng chẵn (như Bomberman classic)
                elif x % 2 == 0 and y % 2 == 0:
                    row.append(WALL)
                # Destructible walls (random)
                elif (x + y) % 3 == 0 and not (x < 3 and y < 3):  # Không đặt gần spawn
                    row.append(DESTRUCTIBLE_WALL)
                else:
                    row.append(EMPTY)
            grid.append(row)
        
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
