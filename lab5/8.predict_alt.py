from time import sleep

from sense_hat import SenseHat


def calculate_altitude(pressure):
    P0 = 1013.25

    altitude = 44331 * (1 - (pressure / P0) ** (1/5.2558))
    return altitude


def main():
    sense = SenseHat()

    while True:
        pressure = sense.get_pressure()

        altitude = calculate_altitude(pressure)

        print("Estimated Altitude: {:.2f} meters".format(altitude))
        sleep(1)


if __name__ == "__main__":
    main()
