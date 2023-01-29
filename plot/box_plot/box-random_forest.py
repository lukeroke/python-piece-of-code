import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dashstyles = [(5,10), (15,15), (10,8,5,7), '']
colors = ["#FF6002", "#008F00", "b", "#B1001C", ]
linestyless = ['-', '-.', '--', ':']
labels = ['40 containers','60 containers', '80 containers']
# labels = [0.99, 0.95, 0.9, 0.85, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
labels = ['1%', '5%', '10%', '15%', '20%', '30%', '40%',
          '50%', '60%', '70%', '80%', '90%']

def set_fontsize(ax, size='x-large'):
    for label in [ax.title, ax.xaxis.label, ax.yaxis.label]+ax.get_xticklabels()+ax.get_yticklabels():
        label.set_fontsize(size)

# data_RL = []  # data here

data = np.load('sens_score_30.npz')['arr_0'].T * 100
print(data.shape) # (30, 12)


selected_data_index = [0,1,2,3,4,5,7,9,11]
data = data[:, selected_data_index]
# labels = (np.array(labels)[selected_data_index]).tolist()
labels = ['1%', '5%', '10%', '15%', '20%', '30%',
          '50%', '70%', '90%']

width = 4
boxprops_RL = dict(linestyle='-', linewidth=width, color=colors[0])
medianprops_RL = dict(linestyle='-', linewidth=width, color=colors[0])
whiskerprops_RL = dict(linestyle='-', linewidth=width, color=colors[0])

plt.figure(figsize=(15,9))
ax = plt.subplot()
plt.grid(True)
plt.minorticks_off()

bp_RL = plt.boxplot(data)
# bp_RL = plt.boxplot(mse01, positions=np.array(range(len(mse01)))*2.2+1.0, widths=0.4, boxprops=boxprops_RL, medianprops=medianprops_RL,whiskerprops=whiskerprops_RL, capprops=whiskerprops_RL, showfliers=False, patch_artist=True)

plt.grid(True)
plt.xlabel("Percentage of all combinations covered in training set",labelpad=20)
# set_fontsize(ax, 35, 0, 45)
set_fontsize(ax, 35)
plt.xticks(list(range(1, len(labels)+1)), labels)
# plt.xticks(list(labels))
# plt.ticklabel_format(style='sci',scilimits=(-3,4),axis='y')
# plt.yticks(fontsize=30)
plt.ylabel("Mean Square Error on test set (in %)",labelpad=20, fontsize=30)
plt.tight_layout(h_pad=2.5)

plt.savefig("./hitestbed_random_forest_box" + ".eps", format='eps', dpi=2400,transparent=True)

# plt.show()