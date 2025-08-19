import pygame
from core.constants import *

class InputHandler:
    def __init__(self):
        self.keys_pressed = set()
        self.keys_just_pressed = set()
        self.movement_timer = 0
        self.movement_delay = 150  # milliseconds between moves
    
    def update(self, events, dt):
        self.keys_just_pressed.clear()
        
        # Handle events
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.keys_just_pressed.add(event.key)
        
        # Handle held keys
        keys = pygame.key.get_pressed()
        self.keys_pressed = set()
        for i, pressed in enumerate(keys):
            if pressed:
                self.keys_pressed.add(i)
        
        # Update movement timer
        if self.movement_timer > 0:
            self.movement_timer -= dt
    
    def get_movement_direction(self):
        if self.movement_timer > 0:
            return None
            
        direction = None
        
        if pygame.K_UP in self.keys_pressed or pygame.K_w in self.keys_pressed:
            direction = UP
        elif pygame.K_DOWN in self.keys_pressed or pygame.K_s in self.keys_pressed:
            direction = DOWN
        elif pygame.K_LEFT in self.keys_pressed or pygame.K_a in self.keys_pressed:
            direction = LEFT
        elif pygame.K_RIGHT in self.keys_pressed or pygame.K_d in self.keys_pressed:
            direction = RIGHT
        
        if direction:
            self.movement_timer = self.movement_delay
            
        return direction
    
    def is_bomb_key_pressed(self):
        return pygame.K_SPACE in self.keys_just_pressed
    
    def is_quit_requested(self):
        return pygame.K_ESCAPE in self.keys_just_pressed