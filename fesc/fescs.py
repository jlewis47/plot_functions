import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binned_statistic
from halo_properties.utils.utils import gather_h5py_files, ll_to_fof_suffix, get_r200_suffix, get_suffix
from halo_properties.utils.output_paths import gen_paths
from halo_properties.params.params import *
from halo_properties.utils.functions_latest import get_infos
import os
import h5py
# from generic.stat import xy_stat
from generic.plot_functions import plot_xy




def fesc_plot(fig, ax, masses, fescs, labels, fesc_type, out_nb):


    fesc_labels = {'gas':"$\mathrm{f_{esc, g}}$",
                'dust':"$\mathrm{f_{esc, d}}$",
                'full':"$\mathrm{f_{esc, gxd}}$"}

    # plot_args = {'ls':'-', 'lw':3}

    xy_plot(fig, ax, masses, fescs, legend=True, labels=labels,
    xlabel='$\mathrm{Halo \, \, masses, \, M_\odot}$', ylabel=fesc_labels[fesc_type],
    xscale='log', yscale='log')        

    if not os.path.isdir('./figs'): os.makedirs('./figs')

    ax.set_title(f'snapshot {out_nb:d}, only star forming haloes')

    # fig.savefig(f'./figs/fesc_comparison_{fesc_type:s}_{out_nb:d}')

    return(fig, ax)

