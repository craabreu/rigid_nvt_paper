import numpy as np
import utility_belt as ub
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
plt.rcParams.update({'font.size':8})
rc('text', usetex=True)

fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharex=True,sharey=False)  
ax = (ax1,ax2,ax3,ax4)
fig.subplots_adjust(hspace=0.1,wspace=0.22)
fig.set_size_inches(w=7.5,h=4)

ax[2].set_xlabel('$h$ (fs)')
ax[3].set_xlabel('$h$ (fs)')

ax[0].set_ylabel(r'T (K)')
ax[1].set_ylabel(r'$<U/N>$ (kcal/mol)')
ax[2].set_ylabel(r'$<W>/N$ (kcal/mol)')
ax[3].set_ylabel(r'$C_v$ (kcal/mol K)')


ax[1].set_xlim(0.5,7.5)
ax[2].set_xlim(0.5,7.5)
xticks = [1,2,3,4,5,6,7]
ax[1].set_xticks(xticks)
ax[2].set_xticks(xticks)
timesteps = [1,2,3,4,5,6,7]
lw = 0.5
NB = 903
kB = 0.0019872041 #Boltzmann's constant (kcal/mol/K).
beta = 1./(kB*298.0)
integrators = ['S1','S1m','P1','K2']
colors = ['blue','magenta','green','red']
labels = ['This work (Unsplit)','This work (NO-SQUISH)', r'Martyna \textit{et al.}', r'Kamberaj \textit{et al.}']
k = 0
for i in integrators:
    data = np.genfromtxt(i + '.csv', delimiter=',', skip_header=1, names=[' ','T','f','df','temperatura',\
                     'dtemperatura','P','dP','E','dE','virial','dvirial','KEtotal','dKEtotal', \
                     'KEt','dKEt','KEr','dKEr','Cv1','dCv1','dfdT','ddfdT'])
    ax[0].errorbar(timesteps, data['temperatura'][0:7],yerr = data['dtemperatura'][0:7],linestyle ='-', color = colors[k], marker = 's',markersize = 4, linewidth = lw, label = labels[k])
    ax[1].errorbar(timesteps, data['P'][0:7],yerr = data['dP'][0:7],linestyle ='-', color = colors[k], marker = 's',markersize = 4, linewidth = lw, label = labels[k])
    ax[2].errorbar(timesteps, data['virial'][0:7],yerr = data['dvirial'][0:7],linestyle ='-', color = colors[k], marker = 's',markersize = 4, linewidth = lw, label = labels[k])
    ax[3].errorbar(timesteps, data['Cv1'][0:7],yerr = data['dCv1'][0:7],linestyle ='-', color = colors[k], marker = 's',markersize = 4, linewidth = lw, label = labels[k])
    k = k + 1
ax[0].axhline(y=298.0, color='black', linestyle='dotted',linewidth=1.0)
ax[1].axhline(y=-9.1028, color='black', linestyle='dotted',linewidth=1.0)
ax[2].axhline(y=-1.776, color='black', linestyle='dotted',linewidth=1.0)
ax[3].axhline(y=17.512, color='black', linestyle='dotted',linewidth=1.0)
ax[0].legend(loc='upper center', bbox_to_anchor=(1.1,1.2), ncol=4, fancybox=True, frameon=False, numpoints = 1)
fig.savefig('thermodynamic_properties.eps', format='eps', dpi=600, bbox_inches='tight')

