import csv
from bokeh.plotting import figure
from bokeh.io import show

dates = range(82)
# with open("../data/ontario-time-series-combined.csv") as file:
#     reader = csv.DictReader(file)

#     dates = [row['Date'] for row in reader]

with open("../data/ontario-time-series-combined.csv") as file:
    reader = csv.DictReader(file)
    confirmed = [row['Confirmed'] for row in reader]

with open("../data/ontario-time-series-combined.csv") as file:
    reader = csv.DictReader(file)
    deaths = [row['Deaths'] for row in reader]

plot = figure(width=400, plot_height=400, title="Confirmed Ontario Cases, 2020")
plot.line(dates, confirmed, line_width=2)
plot.line(dates, deaths, line_width=2)

show(plot)