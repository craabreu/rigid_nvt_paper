import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import mics
import pandas as pd
plt.rcParams.update({'font.size':8})

fig = plt.figure('axes',figsize=(3,2))
ax = fig.add_subplot(111)
ax.set_xlabel('$h$ (fs)')
ax.set_ylabel('$\Delta F/N$ (kcal/mol)')
timesteps = [1,2,3,4,5,6,7]
color = ['blue', 'green', 'red', 'black' ]
ax.set_xlim(0.5,7.5)
xticks = [1,2,3,4,5,6,7]
ax.set_xticks(xticks)

Ts = [298.00,297.99,297.98,298.01,297.99,298.00,297.99]
Ts_error = [0.01,0.01,0.01,0.01,0.01,0.01,0.01]
lw = 0.5


NB = 903
kB = 0.0019872041 #Boltzmann's constant (kcal/mol/K).
beta = 1./(kB*298.0)
data = np.genfromtxt('S1.csv', delimiter=',', skip_header=1, names=[' ','T','f','df','temperatura',\
                     'dtemperatura','P','dP','E','dE','virial','dvirial','KEtotal','dKEtotal', \
                     'KEt','dKEt','KEr','dKEr','Cv1','dCv1','dfdT','ddfdT'])
ax.errorbar(timesteps, data['f'][0:7]/(NB*beta),yerr = data['df'][0:7]/(NB*beta),linestyle ='-', color = 'black', marker = 'o',markersize = 4, linewidth = lw)
ax2 = ax.twinx()
ax2.set_ylim(297.0,299.0)
yticks = [297.0,298.0,299.0]
ax2.set_yticks(yticks)
ax2.set_ylabel('$T$ (K)')
ax2.errorbar(timesteps, Ts, yerr=Ts_error,linestyle ='-', color = 'red', marker = 's',markersize = 4, linewidth = lw)


#ax.legend(loc='upper center', bbox_to_anchor=(0.5,0.7), ncol=2, fancybox=True, frameon=False, numpoints = 1)
fig.savefig('Free_Energy.eps', format='eps', dpi=600, bbox_inches='tight')
