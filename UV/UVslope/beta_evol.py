import numpy as np
import os
from scipy.stats import binned_statistic
import h5py

from ..utils.utils import get_mod_path
from ..generic.plot_functions import xy_plot
from ..generic.stat import xy_stat


def plot_beta_evol(fig, ax, reds, intercepts, medians):

    xy_plot(
        fig,
        ax,
        [reds, reds],
        [intercepts, medians],
        xlabel="redshift",
        ylabel="$\mathrm{UV \, slope \, \beta}$",
        xscale="linear",
        yscale="log",
    )

    # if not os.path.isdir("./figs/"):
    #     os.makedirs("./figs/")


def get_booststrap_evol(
    redshifts, mags, betas, mag_bins, sim_name, Nboot=10000, overwrite=False
):

    z_str = "_".join(redshifts)

    if not os.isdir("./files"):
        os.makedirs("./files")

    out_file = os.path.join("./files", f"beta_evol_{sim_name:s}_{z_str:s}")

    if not os.path.exists(out_file) or overwrite:

        meds, intercepts = make_bootstrap_evol(
            redshifts, mags, betas, mag_bins, Nboot=Nboot
        )

        with h5py.File(out_file, "w") as dest:

            dest.create_dataset(
                "intercept", data=intercepts, dtype="f4", compression="lzf"
            )
            dest.create_dataset("medians", data=meds, dtype="f4", compression="lzf")
            dest.create_dataset(
                "redshifts", data=redshifts, dtype="f4", compression="lzf"
            )

    else:

        with h5py.File(out_file, "r") as src:
            redshifts, meds, intercepts = src[["redshifts", "medians", "intercepts"]]

    return (redshifts, meds, intercepts)


def make_bootstrap_evol(redshifts, mags, betas, mag_bins, Nboot=10000):

    """
    redshifts is length n
    mags and betas should be (n,m)
    """

    def polyn(x, coefs):

        order = len(coefs) - 1  # two coefs is an order 1 poly etc

        if type(coefs) != list and type(coefs) != tuple and type(coefs) != np.ndarray:
            # coefs is a number assume order 0
            order = 0
            coefs = [coefs]

        poly = np.zeros_like(x)

        for i_ord in range(order + 1):

            poly += x ** (order - i_ord) * coefs[i_ord]

        return poly

    nbs_high = np.zeros((len(redshifts), Nboot))
    meds_high = np.zeros((len(redshifts), Nboot))

    intercepts = np.zeros((len(redshifts), Nboot))

    for i_out in range(len(redshifts)):

        data = betas[i_out]
        mags = mags[i_out]

        loc_nb = len(data[data != 0])
        enough_data = loc_nb > 5

        nbs_high[i_out] = len(data[data != 0][(mags < -18)[data != 0]])

        if np.any(enough_data):

            # fit and get intercept
            # near -19
            tgt_mag = -19.5
            bin_mag_lim = -15

            for istrap in range(Nboot):

                if istrap % 1000 == 0:
                    print("%.2f" % (istrap / float(Nboot) * 100.0))

                strap_ind = np.random.randint(low=0, high=len(mags) - 1, size=len(mags))
                strapd_mags = mags[strap_ind]
                strapd_data = data[strap_ind]

                meds_high[i_out, istrap] = np.median(
                    strapd_data[strapd_data != 0][(strapd_mags < -18)[strapd_data != 0]]
                )

                mag_cond = strapd_mags < bin_mag_lim  # *(strapd_mags>-19.5)

                avg_betas, bins, edges = binned_statistic(
                    strapd_mags[mag_cond],
                    strapd_data[mag_cond],
                    np.median,
                    bins=mag_bins,
                )
                nan_filter = np.isnan(avg_betas) == False

                nbs, bins, loc_bins = binned_statistic(
                    strapd_mags[mag_cond],
                    strapd_data[mag_cond],
                    "count",
                    bins=mag_bins,
                )

                enough_data = nbs > 5

                coefs = np.polyfit(
                    bins[:-1][nan_filter * enough_data],
                    avg_betas[nan_filter * enough_data],
                    deg=2,
                    w=-avg_betas[nan_filter * enough_data],
                )  # weight by -beta so weighted towards brightest
                # print(coefs)
                intercepts[i_out, istrap] = polyn(tgt_mag, coefs)  ##
                # print(intercepts[i_out])

    return (meds_high, intercepts)


def plot_beta_evol_constraints(ax, lines, labels):

    bouwens14_intercept = np.asarray(
        [
            2.5,
            -1.70,
            0.07,
            0.15,
            3.8,
            -1.85,
            0.01,
            0.06,
            5.0,
            -1.91,
            0.02,
            0.06,
            5.9,
            -2.00,
            0.05,
            0.08,
            7.0,
            -2.05,
            0.09,
            0.13,
            8.0,
            -2.13,
            0.44,
            0.27,
        ]
    ).reshape((6, -1))

    bhatawdekar20_z_med_betas = np.asarray(
        [
            [
                8.811106053709603,
                -2.408284023668639,
                -2.1390532544378695,
                -2.5710059171597637,
            ],
            [
                7.91034634858218,
                -2.390532544378698,
                -2.1479289940828403,
                -2.6360946745562135,
            ],
            [
                6.912228014771783,
                -2.2189349112426036,
                -2.0177514792899407,
                -2.390532544378699,
            ],
            [
                5.910111726862777,
                -2.177514792899408,
                -2.1094674556213016,
                -2.284023668639054,
            ],
        ]
    )

    line_bhatawdekar = ax.errorbar(
        bhatawdekar20_z_med_betas[:, 0],
        bhatawdekar20_z_med_betas[:, 1],
        yerr=[
            bhatawdekar20_z_med_betas[:, 1] - bhatawdekar20_z_med_betas[:, 3],
            bhatawdekar20_z_med_betas[:, 2] - bhatawdekar20_z_med_betas[:, 1],
        ],
        markersize=15,
        mew=3,
        capsize=5,
        elinewidth=2,
        capthick=1,
        fmt="H",
        mfc="none",
    )

    line_bouwens = ax.errorbar(
        bouwens14_intercept[:, 0] + 0.05,
        bouwens14_intercept[:, 1],
        yerr=[bouwens14_intercept[:, 2], bouwens14_intercept[:, 2]],
        mfc="none",
        markersize=15,
        mew=3,
        capsize=5,
        elinewidth=2,
        capthick=1,
        fmt="s",
    )

    labels.append(
        [
            r"Bhatawdekar+20, Median $\mathrm{M^{ext}_{AB1600}}$<-18",
            r"Bouwens+14, intercept at $\mathrm{M^{ext}_{AB1600}=-19.5}$",
        ]
    )
    lines.append(line_bhatawdekar, line_bouwens)
