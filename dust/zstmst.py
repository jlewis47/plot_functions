import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
import h5py
from ..utils.utils import get_mod_path
from ..generic.plot_functions import xy_plot

def plot_zstmst(fig, ax, ms, z, redshift=None, **plot_args):


    line = xy_plot(fig, ax, ms, z, xlabel=r"$\mathrm{Stellar \, Mass, \, M_\odot}$", ylabel=r"$\mathrm{Average \, stellar \, metallicity}$",
        **plot_args)

    return(line)

def plot_dustier_zstmst(ax, redshift, zprec=0.1,log=False, **plot_args):

    dir_path = get_mod_path()

    label="DUSTiER"

    with h5py.File(os.path.join(dir_path,"../constraints/dustier_zstmst")) as src:

        keys = list(src.keys())
        # print(keys)
        redshifts = [float(k.split('_')[-1].lstrip('z')) for k in keys if "zst" in k]
        mZ_keys = [k for k in keys if "zst" in k]

        # print(redshifts, mZ_keys)
        
        dist = np.abs(redshift - redshifts)

        # print(keys, redshifts, mdust_keys, dist)
        if np.any(dist):

            whs = np.argmin(dist)

            mstel = src['mst_bins'][()]
            Zst = src[mZ_keys[whs]][()]

            print(mstel, Zst)


            if not log:
                l,=ax.plot(mstel/0.8, Zst, **plot_args)
            else:
                l,=ax.plot(np.log10(mstel/0.8), np.log10(Zst), **plot_args)

            return([l],[label])

        else:

            return([],[""])


def plot_zstmst_constraints(ax, redshift, zprec=0.1):


    dir_path = get_mod_path()

    lines=[]
    labels=[]


    return(lines, labels)