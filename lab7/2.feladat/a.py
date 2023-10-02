import random
from time import sleep

from sense_hat import SenseHat

# Initialize SenseHat, game speed, basket position, and score
sense = SenseHat()
speed = 0.4
basket = [7, 4]
score = 0

# Colors
w = (0, 0, 0)
r = (255, 255, 255)
b = (255, 255, 255)

# Initial game space
game_space = [w] * 64  # Creates a list of 64 elements all initialized to white

# Function to update game space
def update_space(x, y, colour):
    p = x * 8 + y
    game_space[p] = colour
    sense.set_pixels(game_space)


# Function to draw basket
def draw_basket(y):
    update_space(7, y, b)
    update_space(7, y + 1, b)


# Clear previous basket
def clear_basket(y):
    update_space(7, y, w)
    update_space(7, y + 1, w)


# Handler functions for joystick movements
def left(event):
    if event.action == "pressed":
        if basket[1] > 0:
            clear_basket(basket[1])
            basket[1] -= 1
            draw_basket(basket[1])


def right(event):
    if event.action == "pressed":
        if basket[1] + 2 < 8:  # Ensure the basket stays within the screen
            clear_basket(basket[1])
            basket[1] += 1
            draw_basket(basket[1])


# Attach the handler functions to joystick events
sense.stick.direction_left = left
sense.stick.direction_right = right

# Clear the LED matrix and set the initial game state
sense.clear()
draw_basket(basket[1])  # Draw initial basket position

# Game loop
game_alive = True
while game_alive:
    x = 0
    y = random.randint(0, 7)
    d = random.choice([-1, 1])

    update_space(x, y, r)

    while True:
        sleep(speed)
        update_space(x, y, w)

        if x == 7:
            if y == basket[1] or y == basket[1] + 1:
                update_space(x, y, b)
                score += 1
                break
            else:
                game_alive = False
                break

        if y == 7 and d == 1:
            d = -1
        elif y == 0 and d == -1:
            d = 1

        y += d
        x += 1
        update_space(x, y, r)

# Display game over message and score
sense.show_message("Game over!", scroll_speed=0.05, back_colour=w)
sense.show_message("Score: " + str(score), scroll_speed=0.05, back_colour=w)
