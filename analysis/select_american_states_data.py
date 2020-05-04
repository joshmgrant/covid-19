from plotting_tools import plot_us_cases_and_deaths

from bokeh.io import show
from bokeh.layouts import row


show(row(
    plot_us_cases_and_deaths('new york'),
    plot_us_cases_and_deaths('florida')
))
