from time import sleep

from sense_hat import SenseHat

ALTITUDE = 125

sense = SenseHat()


def calculate_sea_level_pressure(P, T, h):
    P0 = P * (1 - 0.0065 * h / (T + 0.0065 * h + 273.15)) ** -5.257
    return P0


def determine_tendency(P0_current, P0_previous):
    if P0_previous is None:
        return None

    difference = P0_current - P0_previous
    if difference > 1.6:
        return 'rising'
    elif difference < -1.6:
        return 'falling'
    else:
        return 'steady'


def predict_weather(tendency, P0):
    if tendency is None:
        return None

    if tendency == 'falling' and 985 <= P0 <= 1050:
        Z = int(127 - 0.12 * P0)
        forecasts = ["Settled Fine", "Fine Weather", "Fine, Becoming Less Settled",
                     "Fairly Fine, Showery Later", "Showery, Becoming More Unsettled",
                     "Unsettled, Rain Later", "Rain at Times, Worse Later",
                     "Rain at Times, Becoming Very Unsettled", "Very Unsettled, Rain"]
        index = max(0, min(Z-1, len(forecasts)-1))
        return forecasts[index]

    elif tendency == 'steady' and 960 <= P0 <= 1033:
        Z = int(144 - 0.13 * P0)
        forecasts = ["Settled Fine", "Fine Weather", "Fine, Possibly Showers",
                     "Fairly Fine, Showers Likely", "Showery, Bright Intervals",
                     "Changeable, Some Rain", "Unsettled, Rain at Times",
                     "Rain at Frequent Intervals", "Very Unsettled, Rain"]
        index = max(0, min(Z-10, len(forecasts)-1))
        return forecasts[index]

    elif tendency == 'rising' and 947 <= P0 <= 1030:
        Z = int(185 - 0.16 * P0)
        forecasts = ["Settled Fine", "Fine Weather", "Becoming Fine",
                     "Fairly Fine, Improving", "Fairly Fine, Possibly Showers Early",
                     "Showery Early, Improving", "Changeable, Mending",
                     "Rather Unsettled, Clearing Later", "Unsettled, Probably Improving",
                     "Unsettled, Short Fine Intervals", "Very Unsettled, Finer at Times",
                     "Stormy, Possibly Improving", "Stormy, Much Rain"]
        index = max(0, min(Z-20, len(forecasts)-1))
        return forecasts[index]


P0_PREVIOUS = None

while True:
    T = sense.get_temperature()
    P = sense.get_pressure()

    P0 = calculate_sea_level_pressure(P, T, ALTITUDE)

    tendency = determine_tendency(P0, P0_PREVIOUS)

    if tendency is not None:
        forecast = predict_weather(tendency, P0)
        if forecast is not None:
            print("Forecast:", forecast)
        else:
            print("Forecast not available for the current conditions.")
    else:
        print("Waiting for sufficient data to determine weather tendency.")

    P0_PREVIOUS = P0
    sleep(1)
