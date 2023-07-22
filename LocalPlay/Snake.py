import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set up the game clock
clock = pygame.time.Clock()

# Define colors
white = (90, 90, 90)
black = (0, 255, 0)
red = (255, 0, 0)

# Define the Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(100, 100)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = black

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x * 10)), (cur[1] + (y * 10)))
        if new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [(100, 100)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (10, 10))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, white, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

# Define the direction constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Define the Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = red
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, window_width // 10) * 10, random.randint(0, window_height // 10) * 10)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (10, 10))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, white, r, 1)

# Create the Snake and Food objects
snake = Snake()
food = Food()

# Main game loop
while True:
    # Handle events
    snake.handle_keys()

    # Move the Snake
    snake.move()

    # Check for collision with the Food
    if snake.get_head_position() == food.position:
        snake.length += 1
        food.randomize_position()

    # Draw the game objects
    window.fill(white)
    snake.draw(window)
    food.draw(window)
    pygame.display.update()

    # Set the game clock
    clock.tick(10)