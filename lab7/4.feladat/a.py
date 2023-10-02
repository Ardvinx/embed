import random
import time

from sense_hat import SenseHat

# Initializing Sense HAT
sense = SenseHat()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initial snake position
snake = [(2, 4), (2, 5), (2, 6)]
direction = "up"

# Initial food position
food = (5, 3)

# Function to draw the game state
def draw_game(snake, food):
    sense.clear()
    for segment in snake:
        sense.set_pixel(segment[0], segment[1], WHITE)

    sense.set_pixel(food[0], food[1], RED)


# Function to update the snake position
def update_snake(snake, direction, food):
    head = snake[0]
    new_head = (head[0], head[1])

    if direction == "up":
        new_head = (head[0], head[1] - 1)
    elif direction == "down":
        new_head = (head[0], head[1] + 1)
    elif direction == "left":
        new_head = (head[0] - 1, head[1])
    elif direction == "right":
        new_head = (head[0] + 1, head[1])

    if new_head == food:
        food = (random.randint(0, 7), random.randint(0, 7))
        snake.insert(0, new_head)
    else:
        snake.insert(0, new_head)
        snake.pop()

    return snake, food


# Game loop
while True:
    # Capture events
    events = sense.stick.get_events()
    for event in events:
        if event.action == "pressed":
            if event.direction == "up":
                direction = "up"
            elif event.direction == "down":
                direction = "down"
            elif event.direction == "left":
                direction = "left"
            elif event.direction == "right":
                direction = "right"

    # Update game state
    snake, food = update_snake(snake, direction, food)

    # Check for collisions
    if (
        snake[0][0] < 0
        or snake[0][0] > 7
        or snake[0][1] < 0
        or snake[0][1] > 7
        or snake[0] in snake[1:]
    ):
        sense.show_message("Game Over!", text_colour=RED)
        break

    # Draw game state
    draw_game(snake, food)

    # Add a delay to control the speed of the game
    time.sleep(0.5)
