import csv
from datetime import datetime
from bokeh.plotting import figure
from bokeh.models import DatetimeTickFormatter
from bokeh.io import show

from model_fitting import confirmed_model


def plot_data(region='ontario', show_estimated=None):
    file_name = '../data/{}-time-series-combined.csv'.format(region)

    with open(file_name) as file:
        reader = csv.DictReader(file)
        actual_dates = [datetime.strptime(row['Date'], '%Y-%m-%d') for row in reader]

    with open(file_name) as file:
        reader = csv.DictReader(file)
        confirmed = [row['Confirmed'] for row in reader]

    with open(file_name) as file:
        reader = csv.DictReader(file)
        deaths = [row['Deaths'] for row in reader]


    plot = figure(width=500, plot_height=600, title="COVID-19 {} Cases, 2020".format(region.capitalize()))
    
    # data
    plot.yaxis.axis_label = "# of Cases"
    plot.xaxis.formatter = DatetimeTickFormatter(days="%m/%d")
    plot.line(actual_dates, confirmed, line_width=2, line_color='red', legend_label='confirmed')
    plot.line(actual_dates, deaths, line_width=2, line_color='blue', legend_label='deaths')
    plot.legend.location = "top_left"

    # model
    if show_estimated:
        model = confirmed_model(region)
        plot.line(actual_dates, model, line_width=2, line_color='red', line_dash='dashed', legend_label="confirmed (model)")

    return plot
