#!/usr/bin/env python3
# coding: utf-8
from matplotlib import pyplot as plt
import matplotlib
import matplotlib.gridspec as gridspec
import numpy as np

from plot_lib import plot_to

@plot_to('figures/plot_bar.pdf')
def plot_bar():
    N = 3
    data_points = (30.4, 18.5, 69.0)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.45       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, data_points, width, yerr=None)
    # p2 = plt.bar(ind, womenMeans, width, bottom=menMeans, yerr=womenStd)

    plt.ylabel('Latency 95th pct')
    plt.title('1/2/5 Cassandra on a 40-vCPU server (fixed)')
    plt.xticks(ind, ('1x40vCPU', '2x20vCPU', '5x8 vCPU'))
    plt.yticks(np.arange(0, 81, 10))
    # plt.legend((p1[0], p2[0]), ('Men', 'Women'))
    # plt.legend(p1, '95th pct')

    # plt.show()


if __name__ == '__main__':
    plot_bar()