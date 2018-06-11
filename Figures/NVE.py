import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import mics
import pandas as pd
plt.rcParams.update({'font.size':8})
fig = plt.figure('axes',figsize=(3.0,2.0)) 
ax = fig.add_subplot(111)
ax.set_xlabel('Time (ns)')
ax.set_ylabel('Total Energy (kcal/mol)')
timesteps = [1,2,3,4]
color = ['blue', 'green', 'red', 'black' ]
ax.set_xlim(-0.1,6.1)
ax.set_ylim(-6480,-6460)
xy = [[(0.8, 0.07),(0.8, 0.42),(0.8, 0.63),(0.8, 0.9)], \
      [(0.87, 0.035),(0.72, 0.2),(0.6, 0.2),(0.47, 0.8)]]

yticks = [-6480,-6475,-6470,-6465,-6460]
ax.set_yticks(yticks)

captions = [r'$h=1$ fs',r'$h=2$ fs',r'$h=3$ fs',r'$h=4$ fs']
color_c = ['black', 'red', 'green', 'blue' ]
k = 0
for i in reversed(timesteps):
    df = pd.read_csv('NVE_' + str(i) + 'fs.csv')
    ax.plot(df['Step']*i*1e-6-0.9, df['TotEng'], color = color[k],label=r'$\mathcal{H}$')
    ax.plot(df['Step']*i*1e-6-0.9, df['Hs'],linestyle = 'dotted', color = color[k],label=r'$\widetilde{\mathcal{H}}$')
    ax.annotate(captions[k], xy=(0, 0) , xycoords= 'axes fraction', xytext=xy[0][k],  \
                 textcoords='axes fraction', color=color_c[k])
    k = k + 1

fig.savefig('NVE.eps', format='eps', dpi=600, bbox_inches='tight')
