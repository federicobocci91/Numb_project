
# This code is freely available, please cite:
# Bocci et al, "Numb prevents a complete EMT by modulating Notch signalling"

import functions as aux
from PyDSTool import *
import PyDSTool as dst
import numpy as np

# set up control case numb=False

numb=False
mir34=False

DSargs          = args(name='Notch_EMT_1cell', checklevel=2)
DSargs.pars     = aux.parameters(onecell=True, numb=numb, mir34=mir34)
DSargs.varspecs = aux.equations(onecell=True, numb=numb, mir34=mir34)
DSargs.fnspecs  = aux.functions()
DSargs.ics      = {'W': 20000.0, 'Z': 40000.0,'Y': 20000.0,'S': 200000.0
	,'N':  0.0e+0, 'D': 0.0e+0, 'J': 0.0e+0, 'I': 20.0e+0}
DSargs.xdomain  = {'W': [0, 5.0e+4],'Z': [0, 5.0e+6],'Y': [0, 5.0e+4],'S': [0, 5.0e+5]
	,'N': [0, 5.0e+5],'D': [0, 5.0e+5],'J': [0, 5.0e+5],'I': [0, 5.0e+5]}
DSargs.pdomain  = {'Dt': [-0.1e+0, 1.0e+4],'Jt': [-0.1e+0, 1.1e+4],'It': [-0.1e+0, 3.0e+3]}
DSargs.tdomain  = [0., 100.0]
DSargs.algparams= {'init_step':1.0e-1}
ODE = Vode_ODEsystem(DSargs)
ODE.set(pars = {'Nt': 1.0e+4, 'gD': 40, 'gJ': 15})

# fig. 1c
freepar = 'Jt'
fp=aux.fast_fixedpoint(ODE)
aux.plot_continuation(ODE, freepar, keys=['W'], ncol=1, nrow=1, LocBifPoints=['LP','B'],bif_startpoint=100,maxstep=1e+4, minstep=1e-1, step=5e+2, silence=True, fs=[6,5], ics=[fp], xlim=[0, 10000])

# fig. 1e
freepar = 'Dt'
fp=aux.fast_fixedpoint(ODE)
aux.plot_continuation(ODE, freepar, keys=['W'], ncol=1, nrow=1, LocBifPoints=['LP','B'],bif_startpoint=10,maxstep=1e+4, minstep=1e-1, step=5e+2, silence=True, fs=[6,5], ics=[fp], xlim=[0, 1000])



# set up numb case numb=True

numb=True
mir34=False
DSargs          = args(name='Notch_EMT_1cell', checklevel=2)
DSargs.pars     = aux.parameters(onecell=True, numb=numb, mir34=mir34)
DSargs.varspecs = aux.equations(onecell=True, numb=numb, mir34=mir34)
DSargs.fnspecs  = aux.functions()
DSargs.ics      = {'W': 20000.0, 'Z': 40000.0,'Y': 20000.0,'S': 200000.0
	,'N':  0.0e+0, 'D': 0.0e+0, 'J': 0.0e+0, 'I': 20.0e+0}
DSargs.xdomain  = {'W': [0, 5.0e+4],'Z': [0, 5.0e+6],'Y': [0, 5.0e+4],'S': [0, 5.0e+5]
	,'N': [0, 5.0e+5],'D': [0, 5.0e+5],'J': [0, 5.0e+5],'I': [0, 5.0e+5]}
DSargs.pdomain  = {'Dt': [-0.1e+0, 1.0e+4],'Jt': [-0.1e+0, 1.1e+4],'It': [-0.1e+0, 3.0e+3]}
DSargs.ics.update({'U':0.75e+6})
DSargs.xdomain.update({'U': [0,5.0e+6]})
DSargs.tdomain  = [0., 100.0]
DSargs.algparams= {'init_step':1.0e-1}


### fig 3B - numb

ODE = Vode_ODEsystem(DSargs)
ODE.set(pars = {'Nt': 1.0e+4, 'gD': 40, 'gJ': 15})
ODE.set(pars = {'U_N': 0.6e+6, 'lN': 0.5, 'lU': 0.6})

# fig. 1d
freepar = 'Jt'
fp=aux.fast_fixedpoint(ODE)
aux.plot_continuation(ODE, freepar, keys=['W'], ncol=1, nrow=1, LocBifPoints=['LP','B'],bif_startpoint=100,maxstep=1e+4, minstep=1e-1, step=5e+2, silence=True, fs=[6,5], ics=[fp], xlim=[0, 10000])

# fig. 1f
freepar = 'Dt'
fp=aux.fast_fixedpoint(ODE)
aux.plot_continuation(ODE, freepar, keys=['W'], ncol=1, nrow=1, LocBifPoints=['LP','B'],bif_startpoint=10,maxstep=1e+4, minstep=1e-1, step=5e+2, silence=True, fs=[6,5], ics=[fp], xlim=[0, 1000])


##########
# include mir34=True to include miR34 post-translational inhibition on Numb
