import pygame
from core.settings import *
from core.constants import *

class Player:
    def __init__(self, x, y, color=BLUE, player_id=1):
        # Vị trí grid
        self.grid_x = x
        self.grid_y = y
        
        # Vị trí pixel (cho smooth movement)
        self.pixel_x = x * TILE_SIZE + (TILE_SIZE - PLAYER_SIZE) // 2
        self.pixel_y = y * TILE_SIZE + (TILE_SIZE - PLAYER_SIZE) // 2
        
        # Target position (cho smooth movement)
        self.target_x = self.pixel_x
        self.target_y = self.pixel_y
        
        # Player properties
        self.color = color
        self.player_id = player_id
        self.alive = True
        self.speed = PLAYER_SPEED
        
        # Bomb properties
        self.max_bombs = 1
        self.bomb_range = 2
        self.bombs_placed = 0
        
        print(f"Player {player_id} spawned at grid ({x}, {y})")
    
    def move(self, direction, game_map):
        # Di chuyển player theo direction nếu có thể
        if not self.alive:
            return False
        
        # Chỉ nhận lệnh di chuyển khi đã đứng đúng tâm ô (grid-aligned)
        if self.pixel_x != self.target_x or self.pixel_y != self.target_y:
            return False
            
        new_x = self.grid_x + direction[0]
        new_y = self.grid_y + direction[1]
        
        print(f"Player {self.player_id} trying to move from ({self.grid_x}, {self.grid_y}) to ({new_x}, {new_y})")
        print(f"Target tile type: {game_map.get_tile(new_x, new_y)} (0=EMPTY, 1=WALL, 2=DESTRUCTIBLE)")
        print(f"Is walkable: {game_map.is_walkable(new_x, new_y)}")
        
        # Check có đi được không
        if game_map.is_walkable(new_x, new_y):
            self.grid_x = new_x
            self.grid_y = new_y
            
            # Update target position cho smooth movement
            self.target_x = new_x * TILE_SIZE + (TILE_SIZE - PLAYER_SIZE) // 2
            self.target_y = new_y * TILE_SIZE + (TILE_SIZE - PLAYER_SIZE) // 2
            
            print(f"Player {self.player_id} moved successfully to ({self.grid_x}, {self.grid_y})")
            return True
        else:
            print(f"Player {self.player_id} cannot move to ({new_x}, {new_y}) - not walkable")
        return False
    
    def update(self):
        # Smooth movement towards target
        dx = self.target_x - self.pixel_x
        dy = self.target_y - self.pixel_y
        
        if abs(dx) > 1:
            self.pixel_x += self.speed if dx > 0 else -self.speed
        else:
            self.pixel_x = self.target_x
            
        if abs(dy) > 1:
            self.pixel_y += self.speed if dy > 0 else -self.speed
        else:
            self.pixel_y = self.target_y
    
    def can_place_bomb(self):
        # Check có thể đặt bom không
        return self.bombs_placed < self.max_bombs
    
    def place_bomb(self):
        # Đặt bom (logic sẽ handle ở game.py)
        if self.can_place_bomb():
            self.bombs_placed += 1
            return True
        return False
    
    def bomb_exploded(self):
        # Gọi khi bom nổ để giảm bomb count
        if self.bombs_placed > 0:
            self.bombs_placed -= 1
    
    def draw(self, screen):
        # Vẽ player
        if self.alive:
            rect = pygame.Rect(
                int(self.pixel_x), 
                int(self.pixel_y), 
                PLAYER_SIZE, 
                PLAYER_SIZE
            )
            pygame.draw.rect(screen, self.color, rect)
            pygame.draw.rect(screen, WHITE, rect, 2)  # Border