#!/usr/bin/env python3
from matplotlib import pyplot as plt
import matplotlib
import numpy as np


FONT_SIZE = 16
TICK_SIZE = 14

def pre_plot_customize():
    plt.cla()
    matplotlib.rcParams.update({
        'font.size': FONT_SIZE,
        'pdf.fonttype': 42,
        'ps.fonttype': 42
    })

def customize_axes(ax):
    if 'set_useOffset' in dir(ax.get_xaxis().get_major_formatter()):
        ax.get_xaxis().get_major_formatter().set_useOffset(False)
    if 'set_scientific' in dir(ax.get_xaxis().get_major_formatter()):
        ax.get_xaxis().get_major_formatter().set_scientific(False)
    for t in [ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels():
        t.set_fontsize(TICK_SIZE)

def post_plot_customize(rect):
    for ax in plt.gcf().get_axes():
        customize_axes(ax)
    plt.tight_layout(rect=rect)

def plot_to(path, rect=None):
    def customize_decorator(func):
        def func_wrapper():
            pre_plot_customize()
            func()
            post_plot_customize(rect)
            for suffix in [ 'eps', 'pdf', 'png', 'jpg', 'svg' ]:
                if path.endswith(suffix):
                    plt.savefig(path, format=suffix)
                    break
            else:
                print(f'Unrecognized suffix in {path}.')
        return func_wrapper
    return customize_decorator
