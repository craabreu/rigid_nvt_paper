import numpy as np
import utility_belt as ub
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
plt.rcParams.update({'font.size':8})
rc('text', usetex=True)

fig,(ax1,ax2,ax3) = plt.subplots(1,3,sharex=True,sharey=True)  
ax = (ax1,ax2,ax3)
fig.subplots_adjust(hspace=0.1,wspace=0.1)
fig.set_size_inches(w=7.5,h=2)

ax[0].set_xlabel('$h$ (fs)')
ax[1].set_xlabel('$h$ (fs)')
ax[2].set_xlabel('$h$ (fs)')

ax[0].set_ylabel(r'{$\langle K \rangle$} (kcal/mol)')
ax[0].set_xlim(0.5,7.5)
ax[1].set_xlim(0.5,7.5)
ax[2].set_xlim(0.5,7.5)

xticks = [1,2,3,4,5,6,7]
ax[0].set_xticks(xticks)
ax[1].set_xticks(xticks)
ax[2].set_xticks(xticks)
timesteps = [1,2,3,4,5,6,7]
lw = 0.5
kB = 0.0019872041 #Boltzmann's constant (kcal/mol/K).
N = 903
beta = 1./(kB*298.0)
integrators = ['S1','P1','K2']
colors = ['black','green','blue']
markers = ['s','^','o','v']
labels = ['Refined/Unsplit', 'Martyna', 'Kamberaj']
k = 0
for i in integrators:
    data = np.genfromtxt(i + '.csv', delimiter=',', skip_header=1, names=[' ','T','f','df','temperatura',\
                     'dtemperatura','P','dP','E','dE','virial','dvirial','KEtotal','dKEtotal', \
                     'KEt','dKEt','KEr','dKEr','Cv1','dCv1','dfdT','ddfdT'])
    ax[k].errorbar(timesteps, data['KEt'][0:7],yerr = data['dKEt'][0:7],linestyle ='-', color = 'blue', marker = 'o', markersize = 4, linewidth = lw, label = r'{$\langle K_t \rangle$}',capsize=2, markeredgewidth=1)
    ax[k].errorbar(timesteps, data['KEr'][0:7],yerr = data['dKEr'][0:7],linestyle ='-', color = 'blue', marker = 's', markersize = 4, linewidth = lw, label = r'{$\langle K_r \rangle$}',capsize=2, markeredgewidth=1)
    ax[k].errorbar(timesteps, (data['KEtotal'][0:7]/(6*N-3))*(3*N-3),yerr =(data['dKEtotal'][0:7]/(6*N-3))*(3*N-3),linestyle ='-', color = 'red', marker = 's', markersize = 4, linewidth = lw, label = r'{$\langle K_t \rangle_{eq}$}', capsize=2,  markeredgewidth=1)
    ax[k].errorbar(timesteps, (data['KEtotal'][0:7]/(6*N-3))*(3*N),yerr = (data['dKEtotal'][0:7]/(6*N-3))*(3*N-3),linestyle ='-', color = 'red', marker = 'o', markersize = 4, linewidth = lw, label = r'{$\langle K_r \rangle_{eq}$}', capsize=2, markeredgewidth=1)
    k = k + 1

ax[1].legend(loc='upper center', bbox_to_anchor=(0.5,0.3), ncol=2, fancybox=True, frameon=False, numpoints = 1)
fig.savefig('energy_partition.eps', format='eps', dpi=600, bbox_inches='tight')

