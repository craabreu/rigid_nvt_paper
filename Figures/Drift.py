import numpy as np
import utility_belt as ub
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import mics
import pandas as pd
plt.rcParams.update({'font.size':8})
from matplotlib import rc

# activate latex text rendering
rc('text', usetex=True)

fig = plt.figure('axes',figsize=(3.37,2))
ax = fig.add_subplot(111)
ax.set_xlabel('$h$ (fs)')
ax.set_ylabel('$R$ (kcal/mol.ns)')


ax.set_xlim(0.5,10.5)
xticks = [1,2,3,4,5,6,7,8,9,10]
ax.set_xticks(xticks)

lw = 0.5

data = np.genfromtxt('Drift.csv', delimiter=',', skip_header=1, names=['timestep','thermo','Hs_nhc_thiswork','Hs_thiswork','H_nhc_martyna','Hs_nve'])
ax.plot(data['timestep'], data['Hs_nhc_thiswork']/data['thermo'],linestyle ='-', color = 'black', marker = 'v',markersize = 4, linewidth = lw, label = r'$\widetilde{H}$ (Refined/Unsplit) ')
ax.plot(data['timestep'], data['H_nhc_martyna']/data['thermo'],linestyle ='-', color = 'green', marker = '^',markersize = 4, linewidth = lw, label = r'$H$ (Martyna) ')
ax.plot(data['timestep'], data['Hs_thiswork']/data['thermo'],linestyle ='-', color = 'red', marker = 's',markersize = 4, linewidth = lw,label = r'$\widetilde{\mathcal{H}}$ (Refined/Unsplit)')
ax.plot(data['timestep'], data['Hs_nve']/data['thermo'],linestyle ='-', color = 'blue', marker = 'o',markersize = 4, linewidth = lw,label = r'$\widetilde{\mathcal{H}}$ (NVE)')

ax.set_ylim(-0.5,4)
ax.legend(loc='upper center', bbox_to_anchor=(0.73,0.95), ncol=1, fancybox=True, frameon=False, numpoints = 1)
fig.savefig('energy_drift.eps', format='eps', dpi=600, bbox_inches='tight')
