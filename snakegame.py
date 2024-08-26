import pygame
import random
import time
import sys
import snake

class SnakeGame:
    def __init__(self, colors, width, height, snake_size=20, speed=15):
        self.WIDTH = width
        self.HEIGHT = height
        self.score = 0

        self.WHITE, self.BLACK, self.RED, self.GREEN = colors

        pygame.init()
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        # # Snake settings
        # self.snake_pos = [[100, 60], [80, 60], [60, 60]]
        # self.snake_direction = 'RIGHT'
        # self.change_to = self.snake_direction

        self.food_pos = self.random_food_position(20)
        self.food_spawn = True

    def random_food_position(self, SNAKE_SIZE):
        return [random.randrange(1, (self.WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
                random.randrange(1, (self.HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]

    def game_over(self):
        font = pygame.font.SysFont('times new roman', 50)
        GO_surf = font.render('Your Score is : ' + str(self.score), True, self.RED)
        GO_rect = GO_surf.get_rect()
        GO_rect.midtop = (self.WIDTH / 2, self.HEIGHT / 4)
        self.win.blit(GO_surf, GO_rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    def draw_food(self, SNAKE_SIZE):
        pygame.draw.rect(self.win, self.RED, pygame.Rect(self.food_pos[0], self.food_pos[1], SNAKE_SIZE, SNAKE_SIZE))


    # draw a grid to help us validate movement, can keep or remove
    def draw_grid(self, SNAKE_SIZE = 20):
        for i in range(self.WIDTH // SNAKE_SIZE):
            pygame.draw.line(self.win, self.WHITE, (i * SNAKE_SIZE, 0),
                             (i * SNAKE_SIZE, self.HEIGHT))
        for i in range(self.HEIGHT // SNAKE_SIZE):
            pygame.draw.line(self.win, self.WHITE, (0, i * SNAKE_SIZE),
                             (self.WIDTH, i * SNAKE_SIZE))

    def run(self):
        # initialize the snake object
        snake1 = snake.Snake(self.win, self.GREEN)
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # event button handling for the snake
            snake1.direction_event_handler(events)

            # move snake based on where the head is
            snake1.move_snake()

            # grow snake if the snake consumed food
            if snake1.snake_pos[0] == self.food_pos:
                self.score += 1
                self.food_spawn = False
            else:
                snake1.snake_pos.pop()

            if not self.food_spawn:
                self.food_pos = self.random_food_position(20)
            self.food_spawn = True

            self.win.fill(self.BLACK)

            self.draw_grid()
            snake1.draw_snake()
            self.draw_food(20)

            # game over conditions per snake can be moved to the snake class
            if (snake1.snake_pos[0][0] < 0 or snake1.snake_pos[0][0] >= self.WIDTH or
                snake1.snake_pos[0][1] < 0 or snake1.snake_pos[0][1] >= self.HEIGHT):
                self.game_over()

            # Game Over conditions
            if snake1.snake_pos[0][0] < 0 or snake1.snake_pos[0][0] > (self.WIDTH - snake1.SNAKE_SIZE):
                self.game_over()
            if snake1.snake_pos[0][1] < 0 or snake1.snake_pos[0][1] > (self.HEIGHT - snake1.SNAKE_SIZE):
                self.game_over()

            pygame.display.update()
            self.clock.tick(snake1.speed)
