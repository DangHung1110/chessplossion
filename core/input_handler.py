import pygame
from core.constants import *

class InputHandler:
    def __init__(self):
        self.keys_pressed = set()
        self.keys_just_pressed = set()
    
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
    
    def get_movement_direction(self):
        # Read current key states directly to avoid any mismatch
        keys = pygame.key.get_pressed()
        
        if keys[K_UP] or keys[K_w]:
            return UP
        if keys[K_DOWN] or keys[K_s]:
            return DOWN
        if keys[K_LEFT] or keys[K_a]:
            return LEFT
        if keys[K_RIGHT] or keys[K_d]:
            return RIGHT
        
        return None
    
    def is_bomb_key_pressed(self):
        return K_SPACE in self.keys_just_pressed
    
    def is_quit_requested(self):
        return K_ESCAPE in self.keys_just_pressed