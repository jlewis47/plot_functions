import numpy as np
import os

from ..utils.utils import get_mod_path
from ..generic.plot_functions import xy_plot
from ..generic.stat import xy_stat


def make_hmsmr(mhalos, mstels, mbins):

    bins, hmsmr = xy_stat(mhalos, mstels, mbins)

    return (bins, hmsmr)


def plot_hmsmr(fig, ax, mhalo, mstel, redshift):

    xy_plot(
        fig,
        ax,
        mhalo,
        mstel,
        xlabel="$\mathrm{Halo \, Mass, \, M_\odot}$",
        ylabel="$\mathrm{Stellar \, Mass, \, M_\odot}$",
        xscale="log",
        yscale="log",
    )

    # if not os.path.isdir("./figs/"):
    #     os.makedirs("./figs/")

    ax.set_title(f"z={redshift:.1f}")


def plot_hmsmr_constraints(ax, redshift):

    dir_path = get_mod_path()

    reed_path = os.path.join(dir_path, "../constraints/read_vals")

    read_st_mass = np.genfromtxt(reed_path, delimiter=",", dtype=float, usecols=7) * 1e7
    read_st_mass_err = (
        np.genfromtxt(reed_path, delimiter=",", dtype=float, usecols=8) * 1e7
    )
    read_M200 = np.genfromtxt(reed_path, delimiter=",", dtype=float, usecols=13) * 1e10
    read_M200_dw = (
        np.genfromtxt(reed_path, delimiter=",", dtype=float, usecols=14) * 1e10
    )
    read_M200_up = (
        np.genfromtxt(reed_path, delimiter=",", dtype=float, usecols=15) * 1e10
    )

    stef21_smhm = np.asarray(
        [
            [5.8, 8.2, 0.14, 10.52, -0.1, 0.05, 0.0],
            [5.8, 8.6, 0.14, 10.79, -0.08, 0.05, 0.0],
            [5.8, 9.0, 0.14, 10.99, -0.07, 0.05, 0.0],
            [5.8, 9.4, 0.14, 11.22, -0.07, 0.05, 0.0],
            [5.8, 9.8, 0.14, 11.43, -0.08, 0.06, 0.0],
            [5.8, 10.2, 0.14, 11.76, -0.08, 0.09, 0.0],
            [5.8, 10.6, 0.14, 11.97, 0.1, 0.1, 1.0],
            [6.79, 8.25, 0.17, 10.61, -0.09, 0.05, 0.0],
            [6.79, 8.7, 0.14, 10.83, -0.08, 0.05, 0.0],
            [6.79, 9.1, 0.14, 11.0, -0.08, 0.05, 0.0],
            [6.79, 9.5, 0.14, 11.19, -0.08, 0.05, 0.0],
            [6.79, 9.9, 0.14, 11.42, -0.09, 0.08, 0.0],
            [6.79, 10.3, 0.14, 11.62, 0.1, 0.1, 1.0],
            [7.68, 8.4, 0.17, 10.71, -0.1, 0.07, 0.0],
            [7.68, 8.9, 0.17, 10.92, -0.09, 0.07, 0.0],
            [7.68, 9.35, 0.14, 11.13, -0.09, 0.07, 0.0],
            [7.68, 9.75, 0.14, 11.31, -0.1, 0.1, 0.0],
            [7.68, 10.15, 0.14, 11.4, 10.1, 0.1, 1.0],
            [8.9, 8.25, 0.17, 10.55, -0.12, 0.12, 0.0],
            [8.9, 8.75, 0.17, 10.85, -0.11, 0.09, 0.0],
            [8.9, 9.5, 0.34, 10.93, 0.1, 0.1, 1.0],
            [9.75, 8.25, 0.17, 10.77, -0.11, 0.1, 0.0],
            [9.75, 8.75, 0.17, 10.76, 0.1, 0.1, 1.0],
        ]
    )

    sphinx_smhm = (
        np.asarray(
            [
                100000000,
                39270.53993252545,
                114815362.14968841,
                41941.64673900447,
                131825673.855641,
                44754.10394941823,
                151356124.84362072,
                50127.744078380514,
                173780082.87493762,
                59017.58744434125,
                199526231.49688828,
                77246.39425683132,
                229086765.276777,
                88142.7579146806,
                263026799.18953815,
                114544.56028172912,
                301995172.0402019,
                144441.89915429152,
                346736850.452531,
                159277.9575326326,
                398107170.5534969,
                210048.48578984692,
                457088189.6148752,
                243209.9002403492,
                524807460.2497734,
                309046.70957475883,
                602559586.0743569,
                428400.9217070371,
                691830970.9189363,
                631458.7966945271,
                794328234.7242821,
                790849.5353184867,
                912010839.3559115,
                1196413.8190153225,
                1047128548.0508986,
                1427974.3801578407,
                1202264434.617413,
                1717868.3111765874,
                1380384264.6028867,
                2090866.9860280147,
                1584893192.4611108,
                2526261.055210491,
                1819700858.6099825,
                3405917.830704826,
                2089296130.8540409,
                4025918.0651703267,
                2398832919.019495,
                5260754.663384785,
                2754228703.3381743,
                6981182.716373583,
                3162277660.1683793,
                8160849.375721778,
                3630780547.7010174,
                11014421.22261635,
                4168693834.7033634,
                12752790.982079046,
                4786300923.22638,
                16441742.489393605,
                5495408738.576248,
                19107206.25689944,
                6309573444.801943,
                23794156.16666592,
                7244359600.749891,
                25661759.077945158,
                8317637711.026709,
                27929866.95176792,
                9549925860.214369,
                38201516.963948585,
                10964781961.43183,
                52602740.32433062,
                12589254117.941713,
                63520623.04181913,
                14454397707.45928,
                79247220.85395549,
                16595869074.375631,
                91723865.35811876,
                19054607179.632523,
                112335719.0227549,
                21877616239.495518,
                147722176.91735175,
                25118864315.09582,
                191251163.47388098,
                28840315031.266117,
                267863022.0671119,
                33113112148.259075,
                382419003.3194733,
                38018939632.05613,
                548863583.8016641,
                43651583224.016655,
                779971193.6362056,
                50118723362.72715,
                1123530280.8202765,
            ]
        )
        .reshape((-1, 2))
        .T
    )

    lines = []
    labels = []

    red_inds = np.abs(redshift - stef21_smhm[:, 0]) < 0.45
    if np.any(red_inds):

        yerr = [
            np.abs(
                10 ** stef21_smhm[red_inds, 1]
                - 10 ** (stef21_smhm[red_inds, 1] - stef21_smhm[red_inds, 2])
            ),
            np.abs(
                -(10 ** stef21_smhm[red_inds, 1])
                + 10 ** (stef21_smhm[red_inds, 1] + stef21_smhm[red_inds, 2])
            ),
        ]
        xerr = [
            np.abs(
                10 ** stef21_smhm[red_inds, 3]
                - 10 ** (stef21_smhm[red_inds, 3] + stef21_smhm[red_inds, 4])
            ),
            np.abs(
                10 ** stef21_smhm[red_inds, 3]
                - 10 ** (stef21_smhm[red_inds, 3] + stef21_smhm[red_inds, 5])
            ),
        ]

        steph_line = ax.errorbar(
            10 ** stef21_smhm[red_inds, 3],
            10 ** stef21_smhm[red_inds, 1],
            xerr=xerr,
            yerr=yerr,
            fmt="x",
            mfc="none",
            mec="k",
            color="k",
            markersize=10,
            xlolims=stef21_smhm[red_inds, -1] == 1.0,
            zorder=15,
        )

        lines.append(steph_line)
        labels.append("Stephanon+21")
    # steph_colors.append(steph_line[0].get_color())

    line_read = ax.errorbar(
        read_M200,
        read_st_mass,
        xerr=[
            -(read_M200 - read_M200_dw) + (read_M200),
            (read_M200 + read_M200_up) - (read_M200),
        ],
        yerr=[
            -(read_st_mass - read_st_mass_err) + (read_st_mass),
            (read_st_mass + read_st_mass_err) - (read_st_mass),
        ],
        fmt="D",
        mfc="none",
        mec="k",
        color="k",
        markersize=10,
        zorder=15,
    )
    label_read = "$\mathrm{z=0}$, Read+2017"

    lines.append(line_read)
    labels.append(label_read)

    line_sphx = ax.plot(
        sphinx_smhm[0], sphinx_smhm[1], linewidth=2, linestyle="-.", color="k"
    )
    label_sphx = "Rosdahl+2018"

    lines.append(line_sphx)
    labels.append(label_sphx)

    return (lines, labels)
