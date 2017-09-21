import functions as aux
import numpy as np
import matplotlib.pyplot as plt
import copy as cp
import matplotlib.colors as cl
from matplotlib import cm
from matplotlib.font_manager import FontProperties


# set up control multi-cell model

np.random.seed(100)

numb=False
mir34=False

p   = aux.parameters(numb=numb, mir34=mir34)
eqs = aux.equations(numb=numb, mir34=mir34)

p['n']  = 50     # number of cells = n x n
p['dt'] = 0.1    # time step of the Euler method

key = 'W'                  # key parameter for hexagonal snapshot plot
clim = [0,40000]           # Color range for the plot
tr  = {'W': [5000, 15000]}

p['t']  = p['dt']
pts_i = aux.euler_traj(eqs, p, pts=None, vlim=aux.vlim(numb=numb))
p['t']  = 120   # time in hours



# fig. 3a - control

p['gD'] = 25
v = 'gJ'
r_v = np.arange(10, 101, 5)
aux.plot_fractionStates(eqs, p, v, r_v, key, tr, pts_i=pts_i, vlim=aux.vlim(numb=numb), show_snapshot=False)

# fig. 3b

p['gJ'] = 45
pts_J045 = aux.euler_traj(eqs, p, pts=pts_i, vlim=aux.vlim(numb=numb))
aux.plot_hex(pts_J045[key], clim=clim, tr=[5000,15000], c=[34000, 22000, 10000], cbar=False)


# fig. 3e

p['gJ'] = 80
pts_J085 = aux.euler_traj(eqs, p, pts=pts_i, vlim=aux.vlim(numb=numb))
aux.plot_hex(pts_J070[key], clim=clim, tr=[5000,15000], c=[34000, 22000, 10000], cbar=False)




# set up NUMB multi-cell model

np.random.seed(100)

numb=True
mir34=False

p   = aux.parameters(numb=numb, mir34=mir34)
eqs = aux.equations(numb=numb, mir34=mir34)

p['n']  = 50     # number of cells = n x n
p['dt'] = 0.1    # time step of the Euler method

key = 'W'                  # key parameter for hexagonal snapshot plot
clim = [0,40000]           # Color range for the plot
tr  = {'W': [5000, 15000]}

p['t']  = p['dt']
pts_i = aux.euler_traj(eqs, p, pts=None, vlim=aux.vlim(numb=numb))

p['t']  = 120   # time in hours

# parameters for multi-cell model
p['U_N'] = 0.6e+6
p['lN'] = 0.7
p['lU'] = 0.6



# fig. 3a - numb

p['gD'] = 25
v = 'gJ'
r_v = np.arange(10, 101, 5)
aux.plot_fractionStates(eqs, p, v, r_v, key, tr, pts_i=pts_i, vlim=aux.vlim(numb=numb), show_snapshot=False)


# fig. 3c

p['gJ'] = 45
pts_J045 = aux.euler_traj(eqs, p, pts=pts_i, vlim=aux.vlim(numb=numb))
aux.plot_hex(pts_J045[key], clim=clim, tr=[5000,15000], c=[34000, 22000, 10000], cbar=False)


# fig. 3f

p['gJ'] = 80
pts_J085 = aux.euler_traj(eqs, p, pts=pts_i, vlim=aux.vlim(numb=numb))
aux.plot_hex(pts_J070[key], clim=clim, tr=[5000,15000], c=[34000, 22000, 10000], cbar=False)




