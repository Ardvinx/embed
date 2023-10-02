import random
import time

from sense_hat import SenseHat

# Initializing Sense HAT
sense = SenseHat()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initial paddle position
paddle_y = 2  # Changed initial position to fit within the new boundaries

# Initial ball position
ball_x = 3
ball_y = random.randint(1, 5)  # Ensure the ball starts above the paddle within new boundaries

# Ball direction
ball_dx = random.choice([-1, 1])
ball_dy = -1  # Make the ball move upwards initially

# Score
score = 0

# Function to draw the game state
def draw_game(paddle_y, ball_x, ball_y):
    sense.clear()
    sense.set_pixel(paddle_y, 7, WHITE)  # Draw paddle
    sense.set_pixel(paddle_y + 1, 7, WHITE)  # Make paddle one pixel longer
    sense.set_pixel(ball_x, ball_y, WHITE)


# Function to update the ball position
def update_ball(ball_x, ball_y, ball_dx, ball_dy, paddle_y):
    ball_x += ball_dx
    ball_y += ball_dy

    if ball_y == 0:  # Ball bounces back from the top
        ball_dy *= -1
    elif ball_y == 7 and paddle_y <= ball_x <= paddle_y + 1:  # Ball hits the paddle
        ball_dy *= -1
        global score
        score += 1
    elif ball_y == 7:  # Player loses if the ball reaches the bottom
        return None, None, None, None

    if ball_x in [1, 6]:  # Ball bounces back from the new sides
        ball_dx *= -1

    return ball_x, ball_y, ball_dx, ball_dy


# Game loop
while True:
    # Capture events
    events = sense.stick.get_events()
    for event in events:
        if event.action == "pressed":
            if event.direction == "left" and paddle_y > 1:  # Updated to fit within new boundaries
                paddle_y -= 1
            elif (
                event.direction == "right" and paddle_y < 5
            ):  # Updated to fit within new boundaries
                paddle_y += 1

    # Update ball position
    ball_x, ball_y, ball_dx, ball_dy = update_ball(ball_x, ball_y, ball_dx, ball_dy, paddle_y)

    if ball_x is None:  # Game over condition
        break

    # Draw game state
    draw_game(paddle_y, ball_x, ball_y)

    # Add a delay to control the speed of the game
    time.sleep(0.3)

# Game over
sense.show_message("Game over! Score: " + str(score), text_colour=WHITE)
