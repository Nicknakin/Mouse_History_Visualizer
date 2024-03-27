import pygame
import sys
from math import floor
import struct

pygame.init()

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = (0, 255, 0)
LINE_COLOR = (255, 255, 255)
LINE_WIDTH = 8
MOUSE_HISTORY = []
MAX_HISTORY = 150

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Mouse_History_Visualizer")

# Open the /dev/input/mice device file
mouse_device = open("/dev/input/mice", "rb")

def get_mouse_event():
    buf = mouse_device.read(3)
    button = buf[0]
    b_left = button & 0x1
    b_middle = (button & 0x4) > 0
    b_right = (button & 0x2) > 0
    x, y = struct.unpack("bb", buf[1:])
    return b_left, b_middle, b_right, x, y

old_x, old_y = (0, 0)
raw_old_x, raw_old_y = (0, 0)
MOUSE_HISTORY.append([(0, 0), (0, 0)])

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    b_left, _, _, x, y = get_mouse_event()
    
    x /= 3
    y /= 3

    new_mouse_x = (old_x + x) % SCREEN_WIDTH
    new_mouse_y = (old_y - y) % SCREEN_HEIGHT

    if new_mouse_x == old_x+x and new_mouse_y == old_y-y:
        MOUSE_HISTORY.append([(old_x, old_y), (new_mouse_x, new_mouse_y)])
    else:
        new_mouse_x, new_mouse_y = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
    old_x, old_y = new_mouse_x, new_mouse_y
    if len(MOUSE_HISTORY) > MAX_HISTORY:
        MOUSE_HISTORY.pop(0)

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the mouse pointer history
    for line in MOUSE_HISTORY:
        pygame.draw.lines(screen, LINE_COLOR, False, line, LINE_WIDTH)

    pygame.display.flip()

# Close the mouse device file
mouse_device.close()

# Quit Pygame
pygame.quit()
sys.exit()
