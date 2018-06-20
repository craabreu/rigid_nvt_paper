import numpy as np
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

ax[0].set_ylabel(r'$T_\textnormal{est}$ (K)')
ax[1].set_ylabel(r'{$\langle U/N \rangle$} (kcal/mol)')
ax[2].set_ylabel(r'{$\langle W/N \rangle$} (kcal/mol)')
ax[3].set_ylabel(r'$C_V$ (cal/mol.K)')


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
integrators = ['P1','S1','S1mr','B1s','K2']
colors = ['red','black','magenta','green','blue']
markers = ['o','s','^','x','v']
labels = [r'Martyna', 'Refined/NHC','Refined/NHC/Miller','Refined/Bussi', r'Kamberaj']
k = 0
for i in integrators:
    data = np.genfromtxt(i + '.csv', delimiter=',', skip_header=1, names=[' ','T','f','df','temperatura',\
                     'dtemperatura','P','dP','E','dE','virial','dvirial','KEtotal','dKEtotal', \
                     'KEt','dKEt','KEr','dKEr','Cv1','dCv1','dfdT','ddfdT'])
    ax[0].errorbar(timesteps, data['temperatura'][0:7],yerr = 1.96*data['dtemperatura'][0:7],linestyle ='-', color = colors[k], marker = markers[k],markersize = 4, linewidth = lw, label = labels[k],capsize=2,   markeredgewidth=1)
    ax[1].errorbar(timesteps, data['P'][0:7],yerr = 1.96*data['dP'][0:7],linestyle ='-', color = colors[k], marker = markers[k],markersize = 4, linewidth = lw, label = labels[k],capsize=2,  markeredgewidth=1)
    ax[2].errorbar(timesteps, data['virial'][0:7],yerr = 1.96*data['dvirial'][0:7],linestyle ='-', color = colors[k], marker = markers[k],markersize = 4, linewidth = lw, label = labels[k],capsize=2,  markeredgewidth=1)
    ax[3].errorbar(timesteps, data['Cv1'][0:7]/0.903,yerr = 1.96*data['dCv1'][0:7]/0.903,linestyle ='-', color = colors[k], marker = markers[k],markersize = 4, linewidth = lw, label = labels[k],capsize=2, markeredgewidth=1)

    k = k + 1

#data = np.genfromtxt('S1wr.csv', delimiter=',', skip_header=1, names=[' ','T','f','df','temperatura',\
#                     'dtemperatura','P','dP','E','dE','virial','dvirial','KEtotal','dKEtotal', \
#                     'KEt','dKEt','KEr','dKEr','Cv1','dCv1','dfdT','ddfdT'])
#ax[0].errorbar(timesteps, data['temperatura'][0:7],yerr = data['dtemperatura'][0:7],linestyle ='-', color = 'red', marker = 'x',markersize = 4, linewidth = lw, markeredgewidth=0.5,markeredgecolor='red', markerfacecolor='None', label = 'No Reweighting')
#ax[1].errorbar(timesteps, data['P'][0:7],yerr = data['dP'][0:7],linestyle ='-', color = 'red', marker = 'x',markersize = 4, linewidth = lw, markeredgewidth=0.5,markeredgecolor='red', markerfacecolor='None', label = 'No Reweighting')
#ax[3].errorbar(timesteps, data['Cv1'][0:7]/0.903,yerr = data['dCv1'][0:7]/0.903,linestyle ='-', color = 'red', marker = 'x',markersize = 4, linewidth = lw, markeredgewidth=0.5,markeredgecolor='red', markerfacecolor='None', label = 'No Reweighting' )

ax[0].axhline(y=298.0, color='black', linestyle='dotted',linewidth=1.0)
ax[1].axhline(y=(-9.1021-9.1028431-9.102223)/3, color='black', linestyle='dotted',linewidth=1.0)
ax[2].axhline(y=(-1.7799-1.77606-1.776779)/3, color='black', linestyle='dotted',linewidth=1.0)
ax[3].axhline(y=(17.4749+17.51209+17.32699)/(3*0.903), color='black', linestyle='dotted',linewidth=1.0)
ax[0].legend(loc='upper center', bbox_to_anchor=(1.1,1.2), ncol=5, fancybox=True, frameon=False, numpoints = 1)

for (i, text) in enumerate(['(a)', '(b)', '(c)', '(d)']):
    ax[i].annotate(text, xy=(0, 0) , xycoords= 'axes fraction', xytext=(0.02,0.05), textcoords='axes fraction')

fig.savefig('thermodynamic_properties.eps', format='eps', dpi=600, bbox_inches='tight')

