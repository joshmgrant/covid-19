import csv
from datetime import datetime
import numpy as np


def confirmed_model():
    with open("../data/ontario-time-series-combined.csv") as file:
        reader = csv.DictReader(file)
        actual_dates = [datetime.strptime(row['Date'], '%Y-%m-%d') for row in reader]

    with open("../data/ontario-time-series-combined.csv") as file:
        reader = csv.DictReader(file)
        confirmed = [row['Confirmed'] for row in reader]

    with open("../data/ontario-time-series-combined.csv") as file:
        reader = csv.DictReader(file)
        deaths = [row['Deaths'] for row in reader]

    # Use an exponential model with linear regression
    # y = C*exp(a*x)
    # ln(y) = a*x + ln(C)

    x_data = np.array([i+1 for i in range(len(confirmed))])
    y = [float(i) + 0.01 for i in confirmed]
    y_data = np.array(y)

    log_y_data = np.log(y_data)

    curve_fit = np.polyfit(x_data, log_y_data, 1)
    coefficients = [curve_fit[0], np.exp(curve_fit[1])]
    return coefficients

