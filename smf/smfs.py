import numpy as np
import matplotlib.pyplot as plt
from halo_properties.params.params import *
from ..generic.stat import mass_function
from ..generic.plot_functions import mf_plot

import os
import h5py


def make_smf(stellar_masses, bins, box_size):
    """make smf from stellar masses and bins

    Args:
        stellar_masses (_type_): stellar masses in same units as bins
        bins (_type_): bins for smf
        box_size (_type_): size of box in cMpc
    """

    bins, smf_no_units, pois_err = mass_function(stellar_masses, bins)

    return (bins, smf_no_units / box_size**3, pois_err / box_size**3)


def smf_plot(fig, ax, mass_bins, smfs, xerrs=[], yerrs=[], **plot_args):
    # plot_args = {'ls':'-', 'lw':3}

    lines = mf_plot(
        fig,
        ax,
        mass_bins,
        smfs,
        xlabel=r"$\mathrm{Stellar \, \, masses, \,  M_\odot}$",
        ylabel=r"$\mathrm{SMF, \,  M_\odot^{-1}.cMpc^{-3}}$",
        xscale="log",
        yscale="log",
        xerrs=xerrs,
        yerrs=yerrs,
        **plot_args
    )

    if not os.path.isdir("./figs/"):
        os.makedirs("./figs/")

    return lines

    # fig.savefig(f'./figs/smf_comparison_{out_nb:d}')


def get_stefanon21_smf(path):
    with open(path, "r") as src:
        reds = []
        smfs = []
        cur_smf = []
        for il, line in enumerate(src):
            if line[0] == "#":
                continue

            if line[0] == "z":
                reds.append(int(line[1:]))
                if len(cur_smf) > 0:
                    smfs.append(cur_smf)
                cur_smf = []
            else:
                smf_line = np.float32(line.strip("\n").split(","))
                smf_line[2:] *= 1e-4
                cur_smf.append(smf_line)

        smfs.append(cur_smf)

    return (np.asarray(reds), np.asarray(smfs))


def plot_constraints(fig, ax, tgt_zed, zed_prec=0.5, color="k"):
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)

    zeds_stefanon21, smfs_stefanon21 = get_stefanon21_smf(
        os.path.join(dir_path, "../constraints/stefanon_smf_21")
    )

    zeds_kiku20, smfs_kiku20 = get_stefanon21_smf(
        os.path.join(dir_path, "../constraints/kikuchihara20_smf")
    )

    zeds = [zeds_stefanon21, zeds_kiku20]
    smfs = [smfs_stefanon21, smfs_kiku20]
    labs = ["Stefanon+21", "Kikuchihara+20"]
    markers = ["D", "H", "o", "P", "<", "V"]

    labels = []
    lines = []

    for set, zed in enumerate(zeds):
        dist = np.abs(zed - tgt_zed)
        if np.any(dist < zed_prec):
            match_zed = zed[dist < zed_prec]
            match_smf = smfs[set][dist < zed_prec]

            if len(match_smf) == 1:
                match_smf = np.asarray(match_smf[0])
                match_zed = match_zed[0]

            # print(match_smf.shape, match_smf, match_zed)

            if match_smf.shape[1] > 2:
                xerr = [
                    10 ** (match_smf[:, 0] - match_smf[:, 1]),
                    10 ** (match_smf[:, 0] + match_smf[:, 1]),
                ]
                yerr = np.asarray(
                    [
                        (match_smf[:, 2] - match_smf[:, 4]),
                        (match_smf[:, 3] + match_smf[:, 2]),
                    ]
                )

                line = ax.errorbar(
                    10 ** match_smf[:, 0],
                    match_smf[:, 2],
                    xerr=xerr,
                    yerr=yerr,
                    color=color,
                    linestyle="none",
                    capsize=5,
                    marker=markers[set],
                )

            else:
                xerr = 0.0
                yerr = 0.0

                line = ax.errorbar(
                    match_smf[:, 0],
                    match_smf[:, 1],
                    xerr=xerr,
                    yerr=yerr,
                    color=color,
                    linestyle="none",
                    capsize=0,
                    marker=markers[set],
                )

            lines.append(line)
            labels.append(labs[set])

    return (lines, labels)
