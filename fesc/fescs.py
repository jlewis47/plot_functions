import numpy as np
import matplotlib.pyplot as plt
import os
# from generic.stat import xy_stat
from ..generic.plot_functions import xy_plot




def fesc_plot(fig, ax, masses, fescs, fesc_type, redshift, xlabel):


    fesc_labels = {'gas':"$\mathrm{f_{esc, g}}$",
                'dust':"$\mathrm{f_{esc, d}}$",
                'full':"$\mathrm{f_{esc, gxd}}$"}

    # plot_args = {'ls':'-', 'lw':3}

    xy_plot(fig, ax, masses, fescs,
    xlabel=xlabel, ylabel=fesc_labels[fesc_type],
    xscale='log', yscale='log')        

    if not os.path.isdir('./figs'): os.makedirs('./figs')

    ax.set_title(f'z={redshift:.1f}, star forming haloes')

    # fig.savefig(f'./figs/fesc_comparison_{fesc_type:s}_{out_nb:d}')



def fesc_Mh_plot(fig, ax, masses, fescs, fesc_type, redshift):

    fesc_plot(fig, ax, masses, fescs, fesc_type, redshift, xlabel='$\mathrm{Halo \, \, masses, \, M_\odot}$')

def fesc_Mst_plot(fig, ax, masses, fescs, fesc_type, redshift):

    fesc_plot(fig, ax, masses, fescs, fesc_type, redshift, xlabel='$\mathrm{Stellar \, \, masses, \, M_\odot}$')


def plot_Mh_fesc_constraints(ax, redshift):

    pass    

def plot_Mst_fesc_constraints(ax, redshift):

    pass    
