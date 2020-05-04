from plotting_tools import plot_data

from bokeh.io import show
from bokeh.layouts import row


show(row(
    plot_data('ontario', show_estimated=True),
    plot_data('alberta', show_estimated=True),
    plot_data('bc', show_estimated=True)
))
