import pygame
import random
import time
from snakegame import SnakeGame

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game dimensions
WIDTH = 800
HEIGHT = 600

# Snake settings
SNAKE_SIZE = 20
SPEED = 20
colors = (WHITE, BLACK, RED, GREEN)

if __name__ == "__main__":
    game = SnakeGame(colors, WIDTH, HEIGHT, SNAKE_SIZE, SPEED)
    game.run()
