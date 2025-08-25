#!/usr/bin/env python3

import pygame
from core.constants import *

print("Testing constants...")
print(f"UP: {UP}")
print(f"DOWN: {DOWN}")
print(f"LEFT: {LEFT}")
print(f"RIGHT: {RIGHT}")
print(f"K_UP: {K_UP}")
print(f"K_w: {K_w}")
print(f"pygame.K_UP: {pygame.K_UP}")
print(f"pygame.K_w: {pygame.K_w}")

# Test if constants match pygame constants
print(f"K_UP == pygame.K_UP: {K_UP == pygame.K_UP}")
print(f"K_w == pygame.K_w: {K_w == pygame.K_w}")

