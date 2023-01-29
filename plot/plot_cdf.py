#!/usr/bin/env python3
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

from plot_lib import plot_to

@plot_to('figures/plot_cdf.pdf')
def plot_cdf():
    data = np.random.random(60)

    num_bins = 20
    counts, bin_edges = np.histogram (data, bins=num_bins, normed=True)
    cdf = np.cumsum (counts)
    plt.plot (bin_edges[1:], cdf/cdf[-1])
 
    plt.ylabel('CDFs')
    plt.title('CDFs')
    # plt.xticks()
    # plt.yticks(np.arange(0, 81, 10))
    # plt.legend((p1[0], p2[0]), ('Men', 'Women'))
    # plt.legend(p1, '95th pct')

    # plt.show()

    for q in [50, 90, 95, 100]:
        print ("{}%% percentile: {}".format (q, np.percentile(data, q)))


if __name__ == '__main__':
    plot_cdf()