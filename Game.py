from Snake import Snake
from Food import Food
from config import NUMBER_OF_CELLS


class Game:
    def __init__(self, screen, food_surface):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.state = "RUNNING"
        self.score = 0
        self.screen = screen
        self.food_surface = food_surface

    def draw(self):
        self.food.draw(self.screen, self.food_surface)
        self.snake.draw(self.screen)

    def update(self):
        if self.state == "RUNNING":
            self.snake.update()
            self.check_collision_with_food()
            self.check_collision_with_edges()
            self.check_collision_with_tail()

    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_pos(self.snake.body)
            self.snake.add_segment = True
            self.score += 1
            self.snake.eat_sound.play()

    def check_collision_with_edges(self):
        if self.snake.body[0].x == NUMBER_OF_CELLS or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == NUMBER_OF_CELLS or self.snake.body[0].y == -1:
            self.game_over()

    def check_collision_with_tail(self):
        headless_body = self.snake.body[1:]
        if self.snake.body[0] in headless_body:
            self.game_over()

    def game_over(self):
        self.snake.reset()
        self.food.position = self.food.generate_random_pos(self.snake.body)
        self.state = "STOPPED"
        self.score = 0
        self.snake.wall_hit_sound.play()
