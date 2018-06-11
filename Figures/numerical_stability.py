import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
plt.rcParams.update({'font.size':8})
rc('text', usetex=True)

fig,(ax1,ax2) = plt.subplots(2,1,sharex=True,sharey=False)  
ax = (ax1,ax2)
fig.subplots_adjust(hspace=0.1,wspace=0.1)
fig.set_size_inches(w=3.0,h=4)

ax[1].set_xlabel(r' Time (ns)')
ax[0].set_ylabel(r'$H$ (kcal/mol)')
ax[1].set_ylabel(r' Thermostat energies (kcal/mol)')
xy = [[(0.75, 0.13),(0.7, 0.29),(0.5, 0.5),(0.35, 0.84)], \
      [(0.5, 0.41),(0.37, 0.2),(0.24, 0.09),(0.01, 0.01)]]
ax[0].set_ylim(-6560,-5600)

ax[0].set_xlim(-1,18)
ax[1].set_xlim(-1,18)

ax[1].set_ylim(-60000,60000)

xticks = [0,6,12,18]
ax[1].set_xticks(xticks)
objects = ['0','6','12','18']
ax[1].set_xticklabels(objects)


captions = [r'$h=1$ fs',r'$h=2$ fs',r'$h=3$ fs',r'$h=4$ fs']
color = ['magenta','purple','black','red']
k = 0
timesteps = [1,2,3,4]
for j in timesteps:
    df = pd.read_csv('K2_' + str(j) +'fs.csv')
    ax[0].plot(df['Step']*j*1E-6, df['H_nhc'],linewidth = 1,color=color[k])
    ax[0].annotate(captions[k], xy=(0, 0) , xycoords= 'axes fraction', xytext=xy[0][k],  \
                 textcoords='axes fraction', color=color[k])
    k = k + 1

k = 0
for j in timesteps:
    df = pd.read_csv('K2_' + str(j) +'fs.csv')
    ax[1].plot(df['Step']*j*1E-6, df['H_nhc1'],linewidth = 1,color=color[k])
    ax[1].plot(df['Step']*j*1E-6, df['H_nhc2'],linewidth = 1,color=color[k])
    ax[1].annotate(captions[k], xy=(0, 0) , xycoords= 'axes fraction', xytext=xy[1][k],  \
                 textcoords='axes fraction', color=color[k])
    k = k + 1
ax[0].annotate('(a)', xy=(0, 0) , xycoords= 'axes fraction', xytext=(0.02,0.9),  \
                 textcoords='axes fraction')
ax[1].annotate('(b)', xy=(0, 0) , xycoords= 'axes fraction', xytext=(0.02,0.9),  \
                 textcoords='axes fraction')


fig.savefig('numerical_stability.eps', format='eps', dpi=600, bbox_inches='tight')
