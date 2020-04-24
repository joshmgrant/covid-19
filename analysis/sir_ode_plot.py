import numpy as np
from scipy.integrate import solve_ivp
from bokeh.plotting import figure
from bokeh.io import show


beta = 3.0
gamma = 2.0

def func(t, u, b, g):
    s = u[0]
    i = u[1]
    r = u[2]
    return [-b * i * s / 14.0, b * i * s / 14.0 - g * i, g * i]


z0 = (0.0, 1.0, 0.0) 
t_vals = np.linspace(0, 90, 90)
sol = solve_ivp(func, z0, t_vals, args=(beta, gamma), dense_output=True)
z = sol.sol(t_vals)

print(z[0])

plot = figure(width=500, plot_height=600, title="SIR Model, beta {}, gamma {}".format(beta, gamma))
plot.yaxis.axis_label = "Time"
plot.line(t_vals, z[0], line_width=2, line_color='red')
plot.line(t_vals, z[1], line_width=2, line_color='green')

show(plot)
