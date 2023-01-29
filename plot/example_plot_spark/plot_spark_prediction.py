#!/usr/bin/env python3
# coding: utf-8
from matplotlib import pyplot as plt
import matplotlib
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D
import numpy as np

from .plot_lib import plot_to


def add_line(ax, x, y):
    line = Line2D(x, y, lw=0.7, color='black')
    ax.add_line(line)
    line.set_clip_on(False)


@plot_to('figures/spark-prediction.pdf')
def plot_spark_prediction():
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, gridspec_kw={ 'width_ratios': [3, 4] })
    size = fig.get_size_inches()
    fig.set_size_inches(size[0] * 4 / 1.8, size[1] / 1.8)

    # WordCount example
    wc_pred = [ 28294, 14671, 17180, 16328, 13988, 14255 ]
    wc_act = [ 24970, 19011, 17157, 15018, 15494, 18672 ]
    wc_labels = [ '1 core', '2 cores', '3 GB', '7 GB', '2 Gbps', '5 Gbps' ]

    ind = np.arange(len(wc_labels))
    width = 0.3
    rescale = lambda a: [ x / 1000 for x in a ]
    ax1.bar(ind - width / 2, rescale(wc_act),  width, color='None', lw=2.0, hatch='xx',   edgecolor='#E05D25', label='Actual' )
    ax1.bar(ind + width / 2, rescale(wc_pred), width, color='None', lw=2.0, hatch='//',   edgecolor='#6D6DB3', label='Predicted')

    ax1.set_xticklabels([ 'origin' ] + wc_labels)
    ax1.grid(True, linewidth=0.5, linestyle='dotted', axis='y', which='major')
    ax1.set_ylim([0, 30])
    ax1.set_ylabel('Runime (sec)')
    ax1.set_title('WordCount')

    rescale = lambda x: [ e * 10 for e in x ] if type(x) is list else x * 10
    ax1.text(2.12, rescale(-0.8), 'Memory ', fontsize=12)
    ax1.text(4.15, rescale(-0.8), 'Network ', fontsize=12)
    add_line(ax1, [ 2.1, 1.7, 1.7 ], rescale([ -0.7, -0.7, -0.55 ]))
    add_line(ax1, [ 2.95, 3.3, 3.3 ], rescale([ -0.7, -0.7, -0.55 ]))
    add_line(ax1, [ 4.13, 3.6, 3.6 ], rescale([ -0.7, -0.7, -0.55 ]))
    add_line(ax1, [ 5.0, 5.4, 5.4 ], rescale([ -0.7, -0.7, -0.55 ]))

    # PageRank example
    pr_pred = [ 541803, 299372, 178618, 209040, 180927, 152814, 119408, 121169 ]
    pr_act = [ 776782, 278385, 171458, 210416, 166404, 159734, 126505, 121677 ]
    pr_labels = [ '2 cores', '4 cores', '8 cores', '15 GB', '30 GB', '45 GB', '2 Gbps', '5 Gbps' ]

    ind = np.arange(len(pr_labels))
    width = 0.3
    rescale = lambda a: [ x / 100000 for x in a ]
    ax2.bar(ind - width / 2, rescale(pr_act),  width, color='None', lw=2.0, hatch='xx',   edgecolor='#E05D25', label='Actual' )
    ax2.bar(ind + width / 2, rescale(pr_pred), width, color='None', lw=2.0, hatch='//',   edgecolor='#6D6DB3', label='Predicted')


    ax2.set_xticklabels([ 'origin' ] + pr_labels)
    ax2.grid(True, linewidth=0.5, linestyle='dotted', axis='y', which='major')
    ax2.set_ylabel('Runime ($10^2$ sec)')
    ax2.set_ylim([ 0, 8 ])
    ax2.yaxis.set_major_locator(ticker.FixedLocator([ 0, 2, 4, 6 ]))
    ax2.set_title('PageRank')

    rescale = lambda x: [ e / 3 * 8 for e in x ] if type(x) is list else x / 3 * 8
    ax2.text(0.8, rescale(-0.8), 'CPU', fontsize=12)
    add_line(ax2, [ 0.78, -0.4, -0.4 ], rescale([ -0.7, -0.7, -0.55 ]))
    add_line(ax2, [ 1.2, 2.4, 2.4 ], rescale([ -0.7, -0.7, -0.55 ]))

    ax2.legend()


if __name__ == '__main__':
    plot_spark_prediction()
