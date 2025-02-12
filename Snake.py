import pygame
from pygame import Vector2
from config import (
    CELL_SIZE, OFFSET, DARK_GREEN, EAT_SOUND_PATH, WALL_HIT_SOUND_PATH
)


class Snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)
        self.add_segment = False
        self.eat_sound = pygame.mixer.Sound(EAT_SOUND_PATH)
        self.wall_hit_sound = pygame.mixer.Sound(WALL_HIT_SOUND_PATH)

    def draw(self, screen):
        for segment in self.body:
            segment_rect = (OFFSET + segment.x*CELL_SIZE,
                            OFFSET + segment.y*CELL_SIZE,
                            CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7)

    def update(self):
        self.body.insert(0, self.body[0] + self.direction)
        if self.add_segment:
            self.add_segment = False
        else:
            self.body = self.body[:-1]

    def reset(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)

