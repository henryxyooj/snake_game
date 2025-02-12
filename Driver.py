import sys
import pygame
from pygame import Vector2
from config import (
    CELL_SIZE, NUMBER_OF_CELLS, OFFSET, GREEN, DARK_GREEN,
    TITLE_FONT_SIZE, SCORE_FONT_SIZE, FOOD_IMAGE_PATH,
    SNAKE_UPDATE_INTERVAL, FRAMES_PER_SECOND
)
from Game import Game


def main():
    pygame.init()

    title_font = pygame.font.Font(None, TITLE_FONT_SIZE)
    score_font = pygame.font.Font(None, SCORE_FONT_SIZE)

    screen = pygame.display.set_mode((2*OFFSET + CELL_SIZE*NUMBER_OF_CELLS,
                                      2*OFFSET + CELL_SIZE*NUMBER_OF_CELLS))
    pygame.display.set_caption("Retro Snake")

    food_surface = pygame.image.load(FOOD_IMAGE_PATH)
    clock = pygame.time.Clock()
    game = Game(screen, food_surface)

    SNAKE_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SNAKE_UPDATE, SNAKE_UPDATE_INTERVAL)

    while True:
        for event in pygame.event.get():
            if event.type == SNAKE_UPDATE:
                game.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if game.state == "STOPPED":
                    game.state = "RUNNING"
                if event.key == pygame.K_UP and game.snake.direction != Vector2(0, 1):
                    game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0, -1):
                    game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1, 0):
                    game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1, 0):
                    game.snake.direction = Vector2(1, 0)

        screen.fill(GREEN)
        pygame.draw.rect(screen, DARK_GREEN, (OFFSET - 5, OFFSET - 5, CELL_SIZE*NUMBER_OF_CELLS + 10, CELL_SIZE*
                                              NUMBER_OF_CELLS + 10), 5)
        game.draw()

        title_surface = title_font.render("Retro Snake", True, DARK_GREEN)
        score_surface = score_font.render(str(game.score), True, DARK_GREEN)
        screen.blit(title_surface, (OFFSET - 5, 20))
        screen.blit(score_surface, (OFFSET - 5, OFFSET + CELL_SIZE*NUMBER_OF_CELLS + 10))

        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)


if __name__ == "__main__":
    main()

