import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
import h5py
from ..utils.utils import get_mod_path
from ..generic.plot_functions import xy_plot
from ..generic.stat import xy_stat


def plot_magms(fig, ax, ms, md, redshift=None, **plot_args):


    line = xy_plot(fig, ax, ms, md, xlabel="$\mathrm{Stellar \, Mass, \, M_\odot}$", ylabel="$\mathrm{M_{AB1600}}$",
        xscale='log', yscale='linear',
        **plot_args)

    ylims = ax.get_ylim()
    if ylims[0]<ylims[1]:
        ax.invert_yaxis()

    return(line)

def make_magms(mags, stelms, stelms_bins, mthd="median"):

    return(xy_stat(stelms, mags, stelms_bins, mthd=mthd))



def plot_dustier_magms(ax, redshift, zprec=0.1, **plot_args):

    dir_path = get_mod_path()

    label="DUSTiER"
    
    with h5py.File(os.path.join(dir_path,"../constraints/dustier_magMs")) as src:

        keys = list(src.keys())
        
        redshifts = [float(k.split('_')[-1].lstrip('z')) for k in keys if "mag_z" in k]
        # mdust_keys = [k for k in keys if "mdust" in k]
        mag_keys = [k for k in keys if "mag_z" in k]
        
        dist = np.abs(redshift - redshifts)

        # print(redshifts)

        # print(keys, redshifts, mdust_keys, dist)
        if np.any(dist):

            whs = np.argmin(dist)

            mbins = src['mass_bins'][()]/0.8
            # mags = src[mdust_keys[whs]][()]
            mags = src[mag_keys[whs]][()] - 2.5*np.log10(1./0.8)
            

            # print(mbins, mags)

            l,=ax.plot(mbins, mags, **plot_args)

            return([l],[label])

        else:

            return([],[""])


def plot_magms_constraints(ax, redshift, zprec=0.1):


    dir_path = get_mod_path()

    labels=[]
    lines=[]


    return(lines, labels)