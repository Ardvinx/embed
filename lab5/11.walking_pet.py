import math
from time import sleep

from sense_hat import SenseHat

sense = SenseHat()

b = (0, 0, 0)
w = (255, 255, 255)
l = (210, 105, 30)
k = (139, 69, 19)
p = (255, 182, 193)
b = (70, 130, 180)

cat1 = [
    b, b, b, b, l, b, b, b,
    b, b, b, l, l, b, b, b,
    b, b, l, k, k, l, b, b,
    b, l, k, k, l, l, l, b,
    b, l, l, w, l, k, l, p,
    b, l, k, l, k, l, k, b,
    b, l, l, k, l, l, b, b,
    b, b, b, p, b, b, b, b
]

cat2 = [
    b, b, b, b, l, b, b, b,
    b, b, b, l, l, b, b, b,
    b, b, l, k, k, l, b, b,
    b, l, k, k, l, l, l, b,
    b, l, l, w, l, k, l, b,
    b, l, k, l, k, l, p, b,
    b, w, l, k, k, l, p, b,
    b, p, b, b, b, b, b, b
]


def walk_cat():
    for _ in range(10):
        sense.set_pixels(cat1)
        sleep(0.5)
        sense.set_pixels(cat2)
        sleep(0.5)


def calculate_force(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)


while True:
    walk_cat()
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    force = calculate_force(x, y, z)

    if force > 1.5:
        walk_cat()

    sleep(0.1)
