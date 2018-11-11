import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
plt.rcParams.update({'font.size':8})
rc('text', usetex=True)

fig,((ax2,ax1),(ax3,ax4)) = plt.subplots(2,2,sharex=True,sharey=True)  
ax = (ax1,ax2,ax3,ax4)
fig.subplots_adjust(hspace=0.1,wspace=0.1)
fig.set_size_inches(w=7.5,h=4)


ax[2].set_xlabel('$h$ (fs)')
ax[3].set_xlabel('$h$ (fs)')

ax[0].set_ylabel(r'{$\langle K \rangle$} (kcal/mol)')
ax[1].set_ylabel(r'{$\langle K \rangle$} (kcal/mol)')
ax[2].set_ylabel(r'{$\langle K \rangle$} (kcal/mol)')
ax[3].set_ylabel(r'{$\langle \widetilde{K} \rangle$} (kcal/mol)')
ax[0].set_xlim(0.5,7.5)
ax[0].set_ylim(740,825)

xticks = [1,2,3,4,5,6,7]

ax[2].set_xticks(xticks)
ax[3].set_xticks(xticks)
timesteps = [1,2,3,4,5,6,7]
lw = 0.5
kB = 0.0019872041 #Boltzmann's constant (kcal/mol/K).
N = 903
beta = 1./(kB*298.0)
integrators = ['P1','K2','S1']
colors = ['black','green','blue']
markers = ['s','^','o','v']

data = np.genfromtxt('S1_KEpartition.csv', delimiter=',', skip_header=1, names=[' ','T','f','df','KEt', \
                     'dKEt','KEr','dKEr','Kt_eq','dKt_eq','Kr_eq','dKr_eq'])
ax[3].errorbar(timesteps, data['KEt'][0:7],yerr = data['dKEt'][0:7],linestyle ='-', color = 'black', marker = 'v', markersize = 4, linewidth = lw, label = r'{$\langle K_t \rangle$}',capsize=2, markeredgewidth=1)
ax[3].errorbar(timesteps, data['KEr'][0:7],yerr = data['dKEr'][0:7],linestyle ='-', color = 'black', marker = '^', markersize = 4, linewidth = lw, label = r'{$\langle K_r \rangle$}',capsize=2, markeredgewidth=1)
ax[3].errorbar(timesteps, data['Kt_eq'][0:7],yerr =data['dKt_eq'][0:7],linestyle ='-', color = 'green', marker = 's', markersize = 4, linewidth = lw, label = r'{$\langle K_t \rangle_\textnormal{eq}$}', capsize=2,  markeredgewidth=1)
ax[3].errorbar(timesteps, data['Kr_eq'][0:7],yerr = data['dKr_eq'][0:7],linestyle ='-', color = 'red', marker = 'x', markersize = 4, linewidth = lw, label = r'{$\langle K_r \rangle_\textnormal{eq}$}', capsize=2, markeredgewidth=1)

k = 0
for i in integrators:
    data = np.genfromtxt(i + '.csv', delimiter=',', skip_header=1, names=[' ','T','f','df','temperatura',\
                     'dtemperatura','P','dP','E','dE','virial','dvirial','KEtotal','dKEtotal', \
                     'KEt','dKEt','KEr','dKEr','Cv1','dCv1','dfdT','ddfdT'])
    ax[k].errorbar(timesteps, data['KEt'][0:7],yerr = data['dKEt'][0:7],linestyle ='-', color = 'black', marker = 'v', markersize = 4, linewidth = lw, label = r'{$\langle K_t \rangle$}',capsize=2, markeredgewidth=1)
    ax[k].errorbar(timesteps, data['KEr'][0:7],yerr = data['dKEr'][0:7],linestyle ='-', color = 'black', marker = '^', markersize = 4, linewidth = lw, label = r'{$\langle K_r \rangle$}',capsize=2, markeredgewidth=1)
    ax[k].errorbar(timesteps, (data['KEtotal'][0:7]/(6*N-3))*(3*N-3),yerr =(data['dKEtotal'][0:7]/(6*N-3))*(3*N-3),linestyle ='-', color = 'green', marker = 's', markersize = 4, linewidth = lw, label = r'{$\langle K_t \rangle_\textnormal{eq}$}', capsize=2,  markeredgewidth=1)
    ax[k].errorbar(timesteps, (data['KEtotal'][0:7]/(6*N-3))*(3*N),yerr = (data['dKEtotal'][0:7]/(6*N-3))*(3*N-3),linestyle ='-', color = 'red', marker = 'x', markersize = 4, linewidth = lw, label = r'{$\langle K_r \rangle_\textnormal{eq}$}', capsize=2, markeredgewidth=1)
    k = k + 1


ax[3].annotate('Refined NHC \& Refined Kinetic Energy', xy=(0, 0) , xycoords= 'axes fraction', xytext=(0.08,0.9),  \
                 textcoords='axes fraction')
ax[2].annotate('Refined NHC \& Reweighted Kinetic Energy', xy=(0, 0) , xycoords= 'axes fraction', xytext=(0.08,0.9),  \
                 textcoords='axes fraction')
ax[0].annotate('NHC', xy=(0, 0) , xycoords= 'axes fraction', xytext=(0.08,0.9),  \
                 textcoords='axes fraction')
ax[1].annotate('KLN', xy=(0, 0) , xycoords= 'axes fraction', xytext=(0.08,0.9),  \
  textcoords='axes fraction')

ax[0].annotate('(b)', xy=(0, 0) , xycoords= 'axes fraction', xytext=(0.008,0.9),  \
                 textcoords='axes fraction')
ax[1].annotate('(a)', xy=(0, 0) , xycoords= 'axes fraction', xytext=(0.008,0.9),  \
                 textcoords='axes fraction')
ax[2].annotate('(c)', xy=(0, 0) , xycoords= 'axes fraction', xytext=(0.008,0.9),  \
                 textcoords='axes fraction')
ax[3].annotate('(d)', xy=(0, 0) , xycoords= 'axes fraction', xytext=(0.008,0.9),  \
  textcoords='axes fraction')

ax[0].legend(loc='upper center', bbox_to_anchor=(0.4,0.4), ncol=2, fancybox=True, frameon=False, numpoints = 1)
fig.savefig('energy_partition.eps', format='eps', dpi=600, bbox_inches='tight')

