import numpy as np
import matplotlib.pyplot as plt
import os
# from generic.stat import xy_stat
from ..generic.plot_functions import xy_plot
from ..utils.utils import get_mod_path
import h5py



def fesc_plot(fig, ax, masses, fescs, fesc_type, redshift, xlabel, plot_args={}):


    fesc_labels = {'gas':"$\mathrm{f_{esc, g}}$",
                'dust':"$\mathrm{f_{esc, d}}$",
                'full':"$\mathrm{f_{esc, gxd}}$"}

    # plot_args = {'ls':'-', 'lw':3}

    lines = xy_plot(fig, ax, masses, fescs,
    xlabel=xlabel, ylabel=fesc_labels[fesc_type],
    xscale='log', yscale='log', plot_args=plot_args)        

    # if not os.path.isdir('./figs'): os.makedirs('./figs')

    ax.set_title(f'z={redshift:.1f}, star forming haloes')

    # fig.savefig(f'./figs/fesc_comparison_{fesc_type:s}_{out_nb:d}')
    return(lines)


def fesc_Mh_plot(fig, ax, masses, fescs, fesc_type, redshift, plot_args={}):

    return(fesc_plot(fig, ax, masses, fescs, fesc_type, redshift, xlabel='$\mathrm{Halo \, \, masses, \, M_\odot}$', plot_args=plot_args))

def fesc_Mst_plot(fig, ax, masses, fescs, fesc_type, redshift, plot_args={}):

    return(fesc_plot(fig, ax, masses, fescs, fesc_type, redshift, xlabel='$\mathrm{Stellar \, \, masses, \, M_\odot}$', plot_args=plot_args))


def plot_cosmic_fesc(fig, ax, redshifts, fescs, plot_args={}):

    lines=xy_plot(fig, ax, redshifts, fescs, xlabel='redshift', ylabel='$\mathrm{<f_{esc}>_{Lintr}}$', xscale='linear', yscale='log', plot_args=plot_args)

    ax.invert_xaxis()

    return(lines)


def plot_dustier_fesc(ax, redshift, fkey="fesc", zprec=0.1, plot_args={}):

    dir_path = get_mod_path()

    assert (fkey=="fesc" or fkey=="fesc_total"), "fkey must be either fesc or fesc_total"

    with h5py.File(os.path.join(dir_path,"../constraints/dustier_median_fescs")) as src:

        redshifts = src['redshifts'][()]
        masses = src['mbins'][()]
        fescs = src[fkey][()]

    dist = np.abs(redshift - redshifts)

    if np.any(dist):

        whs = np.argmin(dist)

        l,=ax.plot(masses, fescs[whs], **plot_args)

    label="DUSTiER"

    return([l],[label])

def plot_cosmic_fesc_constraints(ax, redshift):

    dir_path = get_mod_path()

    pass

def plot_Mh_fesc_constraints(ax, redshift):

    dir_path = get_mod_path()

    pass    

def plot_Mst_fesc_constraints(ax, redshift):

    dir_path = get_mod_path()

    pass    
