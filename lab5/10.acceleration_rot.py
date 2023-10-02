from time import sleep

from sense_hat import SenseHat

sense = SenseHat()

while True:
    o = sense.get_orientation()

    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]

    acceleration = sense.get_accelerometer_raw()

    x = round(acceleration['x'], 0)
    y = round(acceleration['y'], 0)
    z = round(acceleration['z'], 0)

    print("pitch:", pitch, "roll:", roll, "yaw:", yaw)
    print("x:", x, "y:", y, "z:", z)
    print()
    sleep(0.5)
