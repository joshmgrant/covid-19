import csv
from datetime import datetime
import numpy as np


def confirmed_model(region='ontario', x_model=[], us_case=None):
    if us_case:
        with open("../scripts/data/us_confirmed_pivot_data.csv") as file:
            reader = csv.DictReader(file)
            confirmed = [row[region.capitalize()] for row in reader]
    else:
        with open("../scripts/data/{}-time-series-combined.csv".format(region)) as file:
            reader = csv.DictReader(file)
            confirmed = [row['Confirmed'] for row in reader]

    # Use an exponential model with linear regression
    # y = C*exp(a*x)
    # ln(y) = a*x + ln(C)

    x_data = np.array([i+1 for i in range(len(confirmed))])
    y_data = [float(i) + 0.01 for i in confirmed]

    log_y_data = np.log(y_data)

    curve_fit = np.polyfit(x_data, log_y_data, 1)
    coef = [curve_fit[0], np.exp(curve_fit[1])]

    # by default, use a [1,2,3...len(x_data)]
    if not x_model:
        x_model = [i+1 for i in range(len(x_data))]

    print('Model for {}: {:.3f}*e^{:.3f}x'.format(region, coef[1], coef[0]))
    return [coef[1]*np.exp(coef[0]*i) for i in x_model]

