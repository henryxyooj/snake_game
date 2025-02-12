import random
import pygame
from pygame import Vector2
from config import CELL_SIZE, NUMBER_OF_CELLS, OFFSET


class Food:
    def __init__(self, snake_body):
        self.position = self.generate_random_pos(snake_body)

    def generate_random_pos(self, snake_body):
        position = self.generate_random_cell()

        while position in snake_body:
            position = self.generate_random_cell()

        return position

    def generate_random_cell(self):
        x = random.randint(0, NUMBER_OF_CELLS - 1)
        y = random.randint(0, NUMBER_OF_CELLS - 1)

        return Vector2(x, y)

    def draw(self, screen, food_surface):
        food_rect = pygame.Rect(OFFSET + self.position.x*CELL_SIZE,
                                OFFSET + self.position.y*CELL_SIZE,
                                CELL_SIZE, CELL_SIZE)
        screen.blit(food_surface, food_rect)
