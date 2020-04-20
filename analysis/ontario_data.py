import csv
from datetime import datetime
from bokeh.plotting import figure
from bokeh.models import DatetimeTickFormatter
from bokeh.io import show

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

    plot = figure(width=500, plot_height=600, title="COVID-19 Ontario Cases, 2020")
    plot.yaxis.axis_label = "# of Cases"
    plot.xaxis.formatter = DatetimeTickFormatter(days="%m/%d")
    plot.line(actual_dates, confirmed, line_width=2, line_color='red', legend_label='confirmed')
    plot.line(actual_dates, deaths, line_width=2, line_color='blue', legend_label='deaths')
    plot.legend.location = "top_left"

    return plot

if __name__ == '__main__':
    show(ontario_plot())
