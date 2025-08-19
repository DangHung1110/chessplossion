
import pygame
import sys
from core.settings import *
from core.map import GameMap
from core.player import Player
from core.input_handler import InputHandler

class Game:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Chessplosion Clone")
        
        self.clock = pygame.time.Clock()
        
        self.game_map = GameMap()
        self.input_handler = InputHandler()

        self.player1 = Player(1, 1, BLUE, 1)  # Top-left spawn
        self.player2 = Player(GRID_WIDTH-2, GRID_HEIGHT-2, RED, 2)  # Bottom-right spawn
        
        self.running = True
        
        print("Game initialized successfully!")
        print(f"Player 1 (Blue): WASD or Arrow keys")
        print(f"Player 2 (Red): Coming soon...")
        print(f"SPACE: Place bomb | ESC: Quit")
    
    def handle_events(self):
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
        
        # Update input handler
        dt = self.clock.get_time()
        self.input_handler.update(events, dt)
        
        # Check quit
        if self.input_handler.is_quit_requested():
            self.running = False
        
        # Handle player movement
        direction = self.input_handler.get_movement_direction()
        if direction:
            moved = self.player1.move(direction, self.game_map)
            if moved:
                print(f"Player moved to ({self.player1.grid_x}, {self.player1.grid_y})")
        
        # Handle bomb placement
        if self.input_handler.is_bomb_key_pressed():
            if self.player1.can_place_bomb():
                print(f"Bomb placed at ({self.player1.grid_x}, {self.player1.grid_y})")
                # TODO: Implement bomb logic
    
    def update(self):
        # Update players
        self.player1.update()
        self.player2.update()
    
    def draw(self):
        # Clear screen
        self.screen.fill(BLACK)
        
        # Vẽ map
        self.game_map.draw(self.screen)
        
        # Vẽ players
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
        
        # Vẽ instructions
        self.draw_instructions()
        
        # Update display
        pygame.display.flip()
    
    def draw_instructions(self):
        font = pygame.font.Font(None, 24)
        instructions = [
            "Arrow Keys/WASD: Move Blue Player",
            "SPACE: Place Bomb",
            "ESC: Quit"
        ]
        
        for i, text in enumerate(instructions):
            text_surface = font.render(text, True, WHITE)
            self.screen.blit(text_surface, (10, 10 + i * 25))
    
    def run(self):
        print("Starting game loop...")
        
        while self.running:
            self.handle_events()
            
            self.update()
            
            self.draw()
            
            # Control FPS
            self.clock.tick(FPS)
        
        # Cleanup
        pygame.quit()
        print("Game closed successfully!")

def main():
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"Error: {e}")
        pygame.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()