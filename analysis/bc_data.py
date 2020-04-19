import csv
from bokeh.plotting import figure
from bokeh.io import show


def bc_plot():

    with open("../data/bc-time-series-combined.csv") as file:
        reader = csv.DictReader(file)
        confirmed = [row['Confirmed'] for row in reader]

    with open("../data/bc-time-series-combined.csv") as file:
        reader = csv.DictReader(file)
        deaths = [row['Deaths'] for row in reader]

    dates = range(len(confirmed))

    plot = figure(width=400, plot_height=600, title="Confirmed BC Cases, 2020")
    plot.line(dates, confirmed, line_width=2, line_color='red')
    plot.line(dates, deaths, line_width=2, line_color='blue')

    return plot

if __name__ == '__main__':
    show(bc_plot())
