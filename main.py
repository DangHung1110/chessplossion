import pygame
import sys
from core.settings import *

class Game:
    def __init__(self):
        # Khởi tạo Pygame
        pygame.init()
        
        # Tạo screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Chessplosion Clone")
        
        # Clock để control FPS
        self.clock = pygame.time.Clock()
        
        # Game state
        self.running = True
        
        print("Game initialized successfully!")
        print(f"Screen size: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        print(f"Grid size: {GRID_WIDTH}x{GRID_HEIGHT}")
        print(f"Tile size: {TILE_SIZE}px")
    
    def handle_events(self):
        """Xử lý events (đóng game, phím nhấn)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    print("Space pressed - sẽ đặt bom ở đây!")
    
    def update(self):
        """Update game logic"""
        # Tạm thời chưa có gì để update
        pass
    
    def draw(self):
        """Vẽ everything lên screen"""
        # Clear screen với màu đen
        self.screen.fill(BLACK)
        
        # Vẽ grid để visualize
        self.draw_grid()
        
        # Vẽ text hướng dẫn
        self.draw_instructions()
        
        # Update display
        pygame.display.flip()
    
    def draw_grid(self):
        """Vẽ lưới để dễ nhìn"""
        for x in range(0, SCREEN_WIDTH, TILE_SIZE):
            pygame.draw.line(self.screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            pygame.draw.line(self.screen, GRAY, (0, y), (SCREEN_WIDTH, y))
    
    def draw_instructions(self):
        """Vẽ text hướng dẫn"""
        font = pygame.font.Font(None, 36)
        
        instructions = [
            "Chessplosion Clone - Basic Setup",
            "ESC: Quit game",
            "SPACE: Place bomb (coming soon)",
            "Arrow keys: Move (coming soon)"
        ]
        
        y_offset = 50
        for i, text in enumerate(instructions):
            color = WHITE if i == 0 else GREEN
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()
            text_rect.centerx = SCREEN_WIDTH // 2
            text_rect.y = y_offset + i * 40
            self.screen.blit(text_surface, text_rect)
    
    def run(self):
        """Main game loop"""
        print("Starting game loop...")
        
        while self.running:
            # Handle input
            self.handle_events()
            
            # Update game
            self.update()
            
            # Draw everything
            self.draw()
            
            # Control FPS
            self.clock.tick(FPS)
        
        # Cleanup
        pygame.quit()
        print("Game closed successfully!")

def main():
    """Entry point"""
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"Error: {e}")
        pygame.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()