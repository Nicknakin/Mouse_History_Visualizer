# Moust_History_Visualizer

# 🖱️ Visualize mouse pointer movement history.
# Press the "X" button in the window to close the visualizer.

# Copyright (C) 2023, Sourceduty - All Rights Reserved.
# THE CONTENTS OF THIS PROJECT ARE PROPRIETARY.

import pygame
import pyautogui
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
BACKGROUND_COLOR = (0, 0, 0)
LINE_COLOR = (255, 255, 255)
LINE_WIDTH = 2
MOUSE_HISTORY = []
MAX_HISTORY = 30

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mouse_History_Visualizer")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current mouse position
    mouse_x, mouse_y = pyautogui.position()
    mouse_x = mouse_x%1920
    mouse_y = mouse_y%1080
    MOUSE_HISTORY.append((mouse_x, mouse_y))
    if len(MOUSE_HISTORY) > MAX_HISTORY:
        MOUSE_HISTORY.pop(0)

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the mouse pointer history
    if len(MOUSE_HISTORY) > 1:
        pygame.draw.lines(screen, LINE_COLOR, False, MOUSE_HISTORY, LINE_WIDTH)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
