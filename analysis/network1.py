import numpy as np
import matplotlib.pyplot as plt

# create an object called a 'node'
class node(object):
  # automatically initialize using prob supplied
  def __init__(self, Pr_S, Pr_I, Pr_R):
    x = np.random.choice( np.array(['S', 'I', 'R']), p = np.array([Pr_S, Pr_I, Pr_R]) )
    if x == 'S':
      self.Susceptible = True
      self.Infective = False
      self.Recovered = False
    elif x =='I':
      self.Susceptible = False
      self.Infective = True
      self.Recovered = False
    else:
      self.Susceptible = False
      self.Infective = False
      self.Recovered = True
    # list of all neighbours
    self.nbrs=[]

# Parameters
#############
pop_size = 1000
Pr_S = 0.98
Pr_I = 1.0 - Pr_S
Pr_R = 0.0
beta = 2.0
gamma = 0.2

# Establish Network
####################
Pr_Edge = 0.05
adj = np.zeros( (pop_size,pop_size), dtype=bool )
for row in range( 1, pop_size ):
  for col in range( row ):
    x = np.random.binomial( 1, Pr_Edge )
    if x == 1:
      adj[row,col] = True
adj = adj + np.transpose(adj)

# Initialize Individuals' State
################################
individual = []
for i in range(pop_size):
  individual = np.append( individual, node(Pr_S, Pr_I, Pr_R) )

for i in range(pop_size):
  individual[i].nbrs = np.arange(pop_size)[ adj[i,:] ]

# Evolve Population Forward in Time
####################################
I_data=np.array([])
t_data=np.array([])

t_elapsed = 0.0
indices = np.arange(pop_size)

# report number of infectives
count=0
for i in indices:
  if individual[i].Infective:
    count+=1

while count > 0:
  # record data
  t_data=np.append(t_data, t_elapsed)
  I_data=np.append(I_data, count)

  # time elapsed between events
  rate = 1.0 / ( (beta+gamma)*count )
  t_elapsed += np.random.exponential( rate )

  # determine what the next event was
  np.random.shuffle(indices)
  for i in indices:
    if individual[i].Infective:
      x=np.random.binomial( 1,gamma/(beta+gamma) )
      if x == 1:
        # recovery
        individual[i].Infective = False
        individual[i].Recovered = True
        count -= 1
      else:
        # transmission
        if len( individual[i].nbrs ) >0:
          nbr_idx = np.random.choice( individual[i].nbrs )
          if individual[nbr_idx].Susceptible:
            individual[nbr_idx].Susceptible = False
            individual[nbr_idx].Infective = True
            count += 1
      break

# Solve Mean Field ODEs
########################
from scipy.integrate import odeint

def sir_eqns( y, x, const1, const2 ):
  u, v = y
  dydt = [ -const1*u*v, const1*u*v - const2*v ]
  return dydt

y0 = [ 1.0 - I_data[0]/pop_size, I_data[0]/pop_size ]
t_vals = np.linspace(0.0, t_elapsed, 101)
soln = odeint(sir_eqns, y0, t_vals, args=(beta, gamma) )

# plot epidemic curve
sim, = plt.plot(t_data, I_data/float(pop_size), '-k', label='Simulated')
ode, =plt.plot(t_vals, soln[:,1], '-r', label='Mean Field ODE')
max1 = np.max( I_data/float(pop_size) )
max2 = np.max(soln[:,1])
my_max = np.max( [max1, max2] )
plt.ylim([0, 1.10*my_max])
plt.xlabel("time", fontsize=14)
plt.ylabel("fraction infected", fontsize=14)
plt.legend(handles=[sim, ode])
plt.show()

