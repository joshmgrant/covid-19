import csv
from datetime import datetime
from bokeh.plotting import figure
from bokeh.models import DatetimeTickFormatter
from bokeh.io import show

from numpy import exp
from ontario_fitting import confirmed_model

def ontario_plot():
    with open("../data/ontario-time-series-combined.csv") as file:
        reader = csv.DictReader(file)
        actual_dates = [datetime.strptime(row['Date'], '%Y-%m-%d') for row in reader]

    with open("../data/ontario-time-series-combined.csv") as file:
        reader = csv.DictReader(file)
        confirmed = [row['Confirmed'] for row in reader]

    with open("../data/ontario-time-series-combined.csv") as file:
        reader = csv.DictReader(file)
        deaths = [row['Deaths'] for row in reader]

    # data
    plot = figure(width=500, plot_height=600, title="COVID-19 Ontario Cases, 2020")
    plot.legend.location = "top_left"    
    plot.yaxis.axis_label = "# of Cases"
    plot.xaxis.formatter = DatetimeTickFormatter(days="%m/%d")
    plot.line(actual_dates, confirmed, line_width=2, line_color='red', legend_label='confirmed')
    plot.line(actual_dates, deaths, line_width=2, line_color='blue', legend_label='deaths')
    
    # model
    A = confirmed_model()
    x = [i+1 for i in range(len(actual_dates))]
    model = [exp(A[1]*i) + exp(A[0]) for i in x]
    plot.line(actual_dates, model, line_width=2, line_color='red', line_dash='dashed', legend_label="confirmed (model)")

    return plot

if __name__ == '__main__':
    show(ontario_plot())
