import numpy as np
from scipy.integrate import odeint
from bokeh.plotting import figure
from bokeh.io import show
from bokeh.layouts import row


def SIR_plot(beta, gamma):
    # recall that R0 = beta / gamma
    def func(y, t, b=beta, g=gamma):
        u, v = y
        return [-b * u * v, b * u * v - g * v]

    t_vals = np.linspace(0, 90, 90)
    y0 = (0.99, 0.01) 
    y = odeint(func, y0, t_vals, args=(beta, gamma))

    plot = figure(width=500, plot_height=600, title="SIR Model, beta {}, gamma {}".format(beta, gamma))
    plot.yaxis.axis_label = "Time"
    plot.line(t_vals, y[:,0], line_width=2, line_color='red')
    plot.line(t_vals, y[:,1], line_width=2, line_color='green')

    return plot

no_outbreak = SIR_plot(1.0, 5.0)
outbreak = SIR_plot(5.0, 1.0)

show(row(no_outbreak, outbreak))
