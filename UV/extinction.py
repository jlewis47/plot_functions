import numpy as np
import os
from scipy.stats import binned_statistic
import h5py

from ..utils.utils import get_mod_path
from ..generic.plot_functions import xy_plot_vect
from ..generic.stat import xy_stat


def make_ext(mags, mags_ext, magbins):
    bins, relation = xy_stat(mags_ext, mags_ext - mags, magbins, mthd="median")

    return (bins, relation)


def plot_ext(fig, ax, mags, ext, redshift=None, **plot_args):
    line = xy_plot_vect(
        fig,
        ax,
        mags,
        ext,
        xlabel="$\mathrm{M^{ext}_{AB1600}}$",
        ylabel=r"$\mathrm{A_{AB1600}}$",
        xscale="linear",
        yscale="linear",
        **plot_args,
    )

    if redshift != None:
        ax.set_title(f"z={redshift:.1f}")

    return line


def plot_dustier_ext(ax, redshift, zprec=0.1, **plot_args):
    dir_path = get_mod_path()

    label = "DUSTiER"

    with h5py.File(os.path.join(dir_path, "../constraints/dustier_exts")) as src:
        keys = list(src.keys())
        redshifts = np.asarray(
            [float(k.split("_")[-1].lstrip("z")) for k in keys if "ext" in k]
        )
        ext_keys = [k for k in keys if "ext" in k]

        dist = np.abs(redshift - redshifts)

        # print(keys, redshifts, mag_keys, dist)
        if np.any(dist):
            whs = np.argmin(dist)

            exts = src[ext_keys[whs]][()]
            bins = src["mag_bins"][()] - 2.5 * np.log10(1.0 / 0.8)

            # print(mags)

            # print(len(bins), len(exts))
            (l,) = ax.plot(bins, exts, **plot_args)

            return ([l], [label])

        else:
            return ([], [""])
