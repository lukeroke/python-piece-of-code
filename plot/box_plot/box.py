import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dashstyles = [(5,10), (15,15), (10,8,5,7), '']
colors = ["#FF6002", "#008F00", "b", "#B1001C", ]
linestyless = ['-', '-.', '--', ':']
labels = ['40 containers','60 containers', '80 containers']


def set_fontsize(ax, size='x-large'):
    for label in [ax.title, ax.xaxis.label, ax.yaxis.label]+ax.get_xticklabels()+ax.get_yticklabels():
        label.set_fontsize(size)

data_RL = []  # data here
width = 4
boxprops_RL = dict(linestyle='-', linewidth=width, color=colors[0])
medianprops_RL = dict(linestyle='-', linewidth=width, color=colors[0])
whiskerprops_RL = dict(linestyle='-', linewidth=width, color=colors[0])

plt.figure(figsize=(15,15))
ax = plt.subplot()
plt.grid(True)
plt.minorticks_off()

bp_RL = plt.boxplot(data_RL, positions=np.array(range(len(data_RL)))*2.2+1.0, widths=0.4, boxprops=boxprops_RL, medianprops=medianprops_RL,whiskerprops=whiskerprops_RL, capprops=whiskerprops_RL, showfliers=False, patch_artist=True)

plt.grid(True)
plt.xlabel("SLA: Normalized Throughput > 1.0",labelpad=20)
set_fontsize(ax, 35, 0, 45)
plt.tight_layout(h_pad=2.5)
plt.ylabel("SLA Satisfaction (%)",labelpad=20, fontsize=35)

plt.savefig("./sla_box" + ".eps", format='eps', dpi=2400,transparent=True)

# plt.show()