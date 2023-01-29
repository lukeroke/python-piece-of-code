#!/usr/bin/env python3
# coding: utf-8
from matplotlib import pyplot as plt
import matplotlib
import matplotlib.ticker as ticker
import numpy as np
import math

from .plot_lib import plot_to


@plot_to('figures/scalability-case.pdf')
def plot_scalability_case():
    fig, ax1 = plt.subplots()
    size = fig.get_size_inches()
    fig.set_size_inches(size[0], size[1] * 7 / 12)

    scale = [ 1, 2, 4, 8 ]
    cpu_speed = [ s / 1e4 for s in [ 14415.07, 15276.53, 26007.60, 35047.14 ] ]
    nccl_speed = [ s / 1e4 for s in [ 13636.11, 24309.82, 43444.80, 70164.44 ] ]

    ax1.plot(scale, cpu_speed, '#E05D25', label='Original', marker='o')
    ax1.plot(scale, nccl_speed, '#6D6DB3', label='Improved', ls='dashed', marker='^')
    ax1.set_xlabel('# GPU')
    ax1.set_ylabel('Training Speed \n ($10^4$ images/sec)')
    ax1.xaxis.set_major_locator(ticker.FixedLocator(scale))
    ax1.yaxis.set_major_locator(ticker.FixedLocator(np.arange(0, 10, 2)))
    # ax1.set_xlim(left=0, right=15)
    ax1.set_ylim(top=8, bottom=0)

    plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower center", ncol=2, edgecolor='None')
    plt.grid(True, linewidth=0.5, linestyle='dotted', axis='y')

if __name__ == '__main__':
    plot_scalability_case()
