import numpy as np
import os
from scipy.stats import binned_statistic
import h5py

from ...utils.utils import get_mod_path
from ...generic.plot_functions import xy_plot_vect
from ...generic.stat import xy_stat


def make_magbeta(mags, betas, magbins):
    bins, relation = xy_stat(mags, betas, magbins, mthd="median")

    return (bins, relation)


def plot_magbeta(fig, ax, mags, betas, redshift=None, **plot_args):
    line = xy_plot_vect(
        fig,
        ax,
        mags,
        betas,
        xlabel="$\mathrm{M_{AB1600}}$",
        ylabel=r"$\mathrm{UV \, slope \, \beta}$",
        xscale="linear",
        yscale="linear",
        **plot_args,
    )

    # if not os.path.isdir("./figs/"):
    #     os.makedirs("./figs/")

    if redshift != None:
        ax.set_title(f"z={redshift:.1f}")

    return line


def plot_dustier_magbeta(ax, redshift, zprec=0.1, **plot_args):
    dir_path = get_mod_path()

    label = "DUSTiER"

    with h5py.File(os.path.join(dir_path, "../constraints/dustier_beta_mag")) as src:
        keys = list(src.keys())
        redshifts = np.asarray(
            [float(k.split("_")[-1].lstrip("z")) for k in keys if "betas" in k]
        )
        beta_keys = [k for k in keys if "betas" in k]

        dist = np.abs(redshift - redshifts)

        # print(keys, redshifts, beta_keys, dist)
        if np.any(dist):
            whs = np.argmin(dist)

            mags = src["mags"][()] - 2.5 * np.log10(1.0 / 0.8)
            betas = src[beta_keys[whs]][()]

            # print(mags)

            (l,) = ax.plot(mags, betas, **plot_args)

            return ([l], [label])

        else:
            return ([], [""])


def plot_magbeta_constraints(ax, redshift, mag_bins, delta_z=0.1):
    """
    TODO:add sim stuff from Wu+20, Shen+20, Vijayan+20/21
    """

    lines = []
    labels = []

    dir_path = get_mod_path()

    plot_dunl13(ax, redshift, mag_bins, dir_path, lines, labels, delta_z=delta_z)
    plot_bouw14(ax, redshift, dir_path, lines, labels, delta_z=delta_z)
    plot_fink12(ax, redshift, mag_bins, dir_path, lines, labels, delta_z=delta_z)
    plot_bhat20(ax, redshift, lines, labels, delta_z=delta_z)

    return (lines, labels)


def plot_dunl13(ax, redshift, mag_bins, dir_path, lines, labels, delta_z=0.1):
    with open(os.path.join(dir_path, "../constraints/dunlop13_betas"), "r") as src:
        dunlop13_full = np.genfromtxt(src, skip_header=1, dtype="<f8")

        ok_z_dunl = np.argwhere(np.abs(redshift - dunlop13_full[:, 0]) < delta_z)
    if len(ok_z_dunl) > 0:
        ok_dunl_mags = np.ravel(np.asarray(dunlop13_full[ok_z_dunl, 1]))
        ok_dunl_betas = np.ravel(np.asarray(dunlop13_full[ok_z_dunl, 2]))
        ok_dunl_betas_error = np.ravel(np.asarray(dunlop13_full[ok_z_dunl, 3]))

        ymed, bins, locs = binned_statistic(
            ok_dunl_mags, ok_dunl_betas, np.nanmedian, bins=mag_bins
        )
        # xmed, bins, locs = binned_statistic(
        #     ok_dunl_mags, ok_dunl_mags, np.nanmedian, bins=mag_bins
        # )

        y75, bins, loc_bins = binned_statistic(
            ok_dunl_mags, ok_dunl_betas, lambda x: np.percentile(x, 84), bins=mag_bins
        )
        y25, bins, loc_bins = binned_statistic(
            ok_dunl_mags, ok_dunl_betas, lambda x: np.percentile(x, 16), bins=mag_bins
        )

        line_dunlp13 = ax.errorbar(
            mag_bins[:-1] + np.diff(mag_bins) * 0.5,
            ymed,
            yerr=[np.abs(ymed - y25), np.abs(y75 - ymed)],
            mfc="none",
            linewidth=3,
            fmt="s",
            drawstyle="steps-mid",
            alpha=0.65,
            markersize=15,
            mew=3,
            capsize=5,
            elinewidth=2,
            capthick=2,
            color="navy",
        )

        lines.append(line_dunlp13)
        labels.append("Dunlop+13")


def plot_bhat20(ax, redshift, lines, labels, delta_z=0.1):
    bhatawdekar20 = np.asarray(
        [
            [
                [-21.38, -2.18, 0.16, 0.15],
                [-19.78, -2.53, 0.17, 0.15],
                [-16.46, -2.26, 0.21, 0.17],
            ],
            [
                [-20.68, -1.93, 0.20, 0.17],
                [-19.56, -2.27, 0.24, 0.20],
                [-17.51, -2.32, 0.30, 0.23],
            ],
            [
                [-20.13, -2.11, 0.34, 0.38],
                [-19.78, -2.26, 0.43, 0.42],
                [-17.12, -2.51, 0.52, 0.45],
            ],
            [
                [-20.90, -2.13, 0.45, 0.42],
                [-19.28, -2.63, 0.52, 0.43],
                [-18.54, -2.51, 0.68, 0.56],
            ],
        ]
    )

    ok_z_bhatawdekar = np.any(
        np.abs(redshift - np.asarray([6.0, 7.0, 8.0, 9.0])) < delta_z
    )

    if ok_z_bhatawdekar:
        zed_ind = int(redshift - 6.0)
        bhatawdekar_mags = bhatawdekar20[zed_ind, :, 0]
        bhatawdekar_betas = bhatawdekar20[zed_ind, :, 1]
        bhatawdekar_ups = bhatawdekar20[zed_ind, :, 2]
        bhatawdekar_dwns = bhatawdekar20[zed_ind, :, 3]

        bwt_line = ax.errorbar(
            bhatawdekar_mags,
            bhatawdekar_betas,
            yerr=[bhatawdekar_dwns, bhatawdekar_ups],
            mfc="none",
            linewidth=3,
            fmt="p",
            drawstyle="steps-mid",
            alpha=0.65,
            markersize=15,
            mew=3,
            capsize=5,
            elinewidth=2,
            capthick=2,
            color="darkgreen",
        )

        lines.append(bwt_line)
        labels.append("Bhatawdekar+20")


def plot_bouw14(ax, redshift, dir_path, lines, labels, delta_z=0.1):
    import csv

    bouwens14_betas = []
    bouwens14_zeds = []
    cur_pack = []

    with open(os.path.join(dir_path, "../constraints/bouwens_2014_beta"), "r") as src:
        spamreader = csv.reader(src, delimiter=" ", quotechar="|")
        for row in spamreader:
            if "z" in row[0]:
                bouwens14_zeds.append(float(row[0].split("=")[-1]))
                if len(cur_pack) > 0:
                    bouwens14_betas.append(np.asarray(cur_pack))
                    cur_pack = []
            else:
                cur_pack.append(np.float32(row[0].split(",")[:-1]))
    bouwens14_betas.append(np.asarray(cur_pack))

    bouwens14_zeds = np.asarray(bouwens14_zeds)

    ok_z_bouw = np.argwhere(np.abs(redshift - bouwens14_zeds) < delta_z)

    if len(ok_z_bouw) > 0:
        # print(ok_z_bouw[0])
        # print(np.asarray(bouwens14_betas))

        ok_bouwens_mags = np.asarray(bouwens14_betas[ok_z_bouw[0][0]])[:, 0]
        ok_bouwens_betas_mean = np.asarray(bouwens14_betas[ok_z_bouw[0][0]])[:, 1]
        ok_bouwens_betas_error = np.asarray(bouwens14_betas[ok_z_bouw[0][0]])[:, 2]

        bouw_line = ax.errorbar(
            ok_bouwens_mags,
            ok_bouwens_betas_mean,
            yerr=ok_bouwens_betas_error,
            color="gold",
            ecolor="gold",
            mfc="none",
            mec="gold",
            fmt="D",
            drawstyle="steps-mid",
        )

        lines.append(bouw_line)
        labels.append("Bouwens+14")


def plot_fink12(ax, redshift, mag_bins, dir_path, lines, labels, delta_z=0.1):
    fink_headers = []
    fink_rows = []

    with open(
        os.path.join(dir_path, "../constraints/finkelstein_2012_data.txt"), "r"
    ) as src:
        for il, line in enumerate(src):
            if "iii" in line:
                continue
            if il <= 28:
                fink_headers.append(line)

            else:
                row = line.strip("\n").strip("").split(" ")
                fink_rows.append([elem for elem in row if elem != ""])

    fink_betas = np.float32([fink_row[7] for fink_row in fink_rows])
    fink_betas_low = np.float32([fink_row[8] for fink_row in fink_rows])
    fink_betas_high = np.float32([fink_row[9] for fink_row in fink_rows])

    fink_mags = np.float32([fink_row[10] for fink_row in fink_rows])
    fink_mags_low = np.float32([fink_row[11] for fink_row in fink_rows])
    fink_mags_high = np.float32([fink_row[12] for fink_row in fink_rows])

    fink_zeds = np.float32([fink_row[4] for fink_row in fink_rows])

    fink12_mag = np.asarray(
        [-17.5, -19.37, -20.55, -18.73, -19.77, -20.27, -20.76, -20.00, -19.53, -19.79]
    )
    fink12_mag_up = np.asarray(
        [-17.39, -19.2, -20.41, -18.52, -19.7, -20.18, -20.67, -19.85, -19.51, -19.47]
    )
    fink12_mag_dw = np.asarray(
        [-17.7, -19.41, -20.58, -18.93, -19.81, -20.39, -20.77, -20.18, -19.66, -20.03]
    )

    fink12_beta = np.asarray(
        [-2.29, -2.38, -2.00, -2.41, -1.95, -2.39, -2.51, -2.37, -2.43, -2.45]
    )
    fink12_beta_up = np.asarray(
        [-2.17, -1.86, -1.83, -2.07, -1.77, -1.91, -2.29, -1.5, -2.02, -1.62]
    )
    fink12_beta_dw = np.asarray(
        [-2.58, -2.41, -2.28, -2.68, -2.01, -2.61, -2.54, -2.68, -2.56, -2.92]
    )

    ok_z_fink = np.argwhere(np.abs(redshift - fink_zeds) < delta_z)
    if len(ok_z_fink) > 0:
        ok_z_betas = np.concatenate(fink_betas[ok_z_fink])
        ok_z_betas_low = np.concatenate(fink_betas_low[ok_z_fink])
        ok_z_betas_high = np.concatenate(fink_betas_high[ok_z_fink])

        ok_z_mags = np.concatenate(fink_mags[ok_z_fink])
        ok_z_mags_low = np.concatenate(fink_mags_low[ok_z_fink])
        ok_z_mags_high = np.concatenate(fink_mags_high[ok_z_fink])

        yavg, bins, locs = binned_statistic(
            ok_z_mags, ok_z_betas, "mean", bins=mag_bins
        )
        xavg, bins, locs = binned_statistic(ok_z_mags, ok_z_mags, "mean", bins=mag_bins)

        y75, bins, locs = binned_statistic(ok_z_mags, ok_z_betas, np.std, bins=mag_bins)
        y25, bins, locs = binned_statistic(ok_z_mags, ok_z_betas, np.std, bins=mag_bins)

        x75, bins, locs = binned_statistic(ok_z_mags, ok_z_mags, np.std, bins=mag_bins)
        x25, bins, locs = binned_statistic(ok_z_mags, ok_z_mags, np.std, bins=mag_bins)
        # ax.errorbar(xavg,yavg,xerr=[xavg-x25,x75-xavg],
        #            yerr=[yavg-y25,y75-yavg],color='k'\

        fink_line = ax.errorbar(
            bins[:-1],
            yavg,
            xerr=x25,
            yerr=y25,
            color="k",
            ecolor="k",
            mfc="none",
            mec="k",
            fmt="D",
        )

        lines += [fink_line]
        labels += ["Finkelstein+14"]
