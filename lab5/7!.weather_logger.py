import time

import matplotlib.pyplot as plt
from sense_hat import SenseHat


def plot(filename):
    temp_list = []
    humi_list = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                values = line.strip().split(',')
                temp_list.append(float(values[0]))
                humi_list.append(float(values[1]))
    except Exception as e:
        print("Error reading file:", e)
        return

    plt.plot(range(1, len(temp_list) + 1),
             temp_list, 'r-', label='Temperature')
    plt.plot(range(1, len(humi_list) + 1), humi_list, 'b--', label='Humidity')
    plt.title('Weather')
    plt.xlabel('Measurements')
    plt.ylabel('Value')
    plt.legend()
    plt.show()


def main():
    sense = SenseHat()
    start_time = time.time()
    stop_time = time.time()
    filename = 'weather.txt'

    with open(filename, 'a') as file:
        print('Data acquisition is starting...')
        while stop_time - start_time < 5:
            temp = sense.get_temperature()
            humidity = sense.get_humidity()
            file.write(str(temp) + ',' + str(humidity) + '\n')
            time.sleep(0.5)
            stop_time = time.time()

    print('Stop data acquisition!')
    plot(filename)


if __name__ == '__main__':
    main()
