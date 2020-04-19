from alberta_data import alberta_plot as ab
from bc_data import bc_plot as bc
from ontario_data import ontario_plot as on

from bokeh.io import show
from bokeh.layouts import row

show(row(ab(), bc(), on()))
