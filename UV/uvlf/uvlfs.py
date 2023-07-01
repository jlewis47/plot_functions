import numpy as np

# import matplotlib.pyplot as plt

from ...generic.stat import mass_function, cosmic_variance
from ...generic.plot_functions import mf_plot
from .LF_constraints_mix import *

import os


def make_uvlf(mags, bins, box_size):
    """make uvlf from stellar mags and bins

    Args:
        mags (_type_): magnitudes in same units as bins
        bins (_type_): bins for uvlf
        box_size (_type_): size of box in cMpc
    """

    bins, uvlf_no_units, err = mass_function(mags, bins, scale="linear")

    return (bins, uvlf_no_units / box_size**3, err / box_size**3)

def make_uvlf_cosmic_var(mags, coords, bins, box_size, sub_size, nsub):
    """assess cosmic variance of uvlf within sim volume

    Args:
        mags (_type_): magnitudes in same units as bins
        coords (double): coords in cMpc
        bins (_type_): bins for uvlf
        box_size (_type_): size of box in cMpc
        sub_size (_type_): size of sub-volumes in cMpc
    """

    cosmic_out = cosmic_variance(lambda mags: mass_function(mags, bins, scale='linear'), 
    mags, coords, box_size**3, sub_size**3, nsub)

    cosmic_uvlf = [out[1] / box_size**3 for out in cosmic_out]

    return (np.percentile(cosmic_uvlf,[10,50,90],axis=0), np.std(cosmic_uvlf,axis=0), np.mean(cosmic_uvlf, axis=0))


def uvlf_plot(fig, ax, mag_bins, uvlfs, redshift=None, xerrs=None, yerrs=None, **plot_args):

    # plot_args = {'ls':'-', 'lw':3}

    lines = mf_plot(
        fig,
        ax,
        mag_bins,
        uvlfs,
        xlabel="$\mathrm{M_{AB1600}}$",
        ylabel="$\mathrm{UVLF, cMpc^{-3}}$",
        xscale="linear",
        yscale="log",
        xerrs=xerrs,
        yerrs=yerrs,
        **plot_args
    )

    if redshift!=None:ax.set_title(f"z={redshift:.1f}")

    ax.invert_xaxis()

    return lines

    # fig.savefig(f'./figs/uvlf_comparison_{out_nb:d}')


def plot_constraints(fig, ax, tgt_zed, prec_zed=0.5, color="k"):

    uvlf_constr_dict = get_LF_constr()

    # print(uvlf_constr_dict.keys())

    # bouwens15_uvlfs = uvlf_constr_dict["bouwens15"]
    # bouwens17_uvlfs = uvlf_constr_dict["bouwens17"]
    bouwens21_uvlfs = uvlf_constr_dict["bouwens21"]
    oesch18_uvlfs = uvlf_constr_dict["oesch18"]
    ono18_uvlfs = uvlf_constr_dict["ono18"]
    ishigaki18_uvlfs = uvlf_constr_dict["ishigaki18"]
    atek18_uvlfs = uvlf_constr_dict["atek18"]
    livermore17_uvlfs = uvlf_constr_dict["livermore17"]
    bowler20_uvlfs = uvlf_constr_dict["bowler20"]
    bouwens22d_uvlfs = uvlf_constr_dict["bouwens22d"]
    bouwens22e_uvlfs = uvlf_constr_dict["bouwens22e"]
    harikane23_uvlfs = uvlf_constr_dict["harikane23"]
    harikane22a_uvlfs = uvlf_constr_dict["harikane22a"]
    donnan22b_uvlfs = uvlf_constr_dict["donnan22b"]
    donnan22e_uvlfs = uvlf_constr_dict["donnan22e"]
    naidu22e_uvlfs = uvlf_constr_dict["naidu22e"]
    finkelstein23a_uvlfs = uvlf_constr_dict["finkelstein23a"]
    

    coda25 = np.array(
        [
            1.51978600e-04,
            0.00000000e00,
            1.51978600e-04,
            3.03957200e-04,
            4.55935801e-04,
            7.59893001e-04,
            1.36780740e-03,
            1.82374320e-03,
            3.95144360e-03,
            5.01529381e-03,
            8.66278021e-03,
            1.21582880e-02,
            1.56537958e-02,
            2.27967900e-02,
            3.13075916e-02,
            4.40737941e-02,
            5.31925101e-02,
            6.85423487e-02,
            8.17644869e-02,
            1.03497427e-01,
            1.23558602e-01,
            1.62617102e-01,
            1.99395923e-01,
            2.33287151e-01,
            3.35112813e-01,
            3.16723403e-01,
            3.00005757e-01,
            3.40736022e-01,
            4.24476230e-01,
            5.64296542e-01,
            7.25545837e-01,
            8.98497484e-01,
            1.07813619e00,
            1.09774143e00,
            1.15746902e00,
            7.29953217e-01,
            2.55628006e-01,
            6.07914401e-04,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            4.49727475e01,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
        ]
    )

    coda25_ext = np.array(
        [
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            1.51978600e-04,
            0.00000000e00,
            1.51978600e-04,
            9.11871601e-04,
            1.82374320e-03,
            3.34352920e-03,
            5.77518681e-03,
            9.11871601e-03,
            1.15503736e-02,
            1.59577530e-02,
            2.26448114e-02,
            3.23714418e-02,
            4.46817085e-02,
            5.28885529e-02,
            6.86943273e-02,
            8.19164655e-02,
            1.03649405e-01,
            1.23558602e-01,
            1.62617102e-01,
            1.99395923e-01,
            2.33287151e-01,
            3.35112813e-01,
            3.16723403e-01,
            3.00005757e-01,
            3.40736022e-01,
            4.24476230e-01,
            5.64296542e-01,
            7.25545837e-01,
            8.98497484e-01,
            1.07813619e00,
            1.09774143e00,
            1.15746902e00,
            7.29953217e-01,
            2.55628006e-01,
            6.07914401e-04,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            4.49727475e01,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
        ]
    )

    coda25_bins = np.array(
        [
            -23.0,
            -22.5,
            -22.0,
            -21.5,
            -21.0,
            -20.5,
            -20.0,
            -19.5,
            -19.0,
            -18.5,
            -18.0,
            -17.5,
            -17.0,
            -16.5,
            -16.0,
            -15.5,
            -15.0,
            -14.5,
            -14.0,
            -13.5,
            -13.0,
            -12.5,
            -12.0,
            -11.5,
            -11.0,
            -10.5,
            -10.0,
            -9.5,
            -9.0,
            -8.5,
            -8.0,
            -7.5,
            -7.0,
            -6.5,
            -6.0,
            -5.5,
            -5.0,
            -4.5,
            -4.0,
            -3.5,
            -3.0,
            -2.5,
            -2.0,
            -1.5,
            -1.0,
            -0.5,
            0.0,
            0.5,
            1.0,
            1.5,
            2.0,
            2.5,
            3.0,
            3.5,
            4.0,
            4.5,
        ]
    )

    codaii_bins = np.array(
        [
            -23.5,
            -23.0,
            -22.5,
            -22.0,
            -21.5,
            -21.0,
            -20.5,
            -20.0,
            -19.5,
            -19.0,
            -18.5,
            -18.0,
            -17.5,
            -17.0,
            -16.5,
            -16.0,
            -15.5,
            -15.0,
            -14.5,
            -14.0,
            -13.5,
            -13.0,
            -12.5,
            -12.0,
            -11.5,
            -11.0,
            -10.5,
            -10.0,
            -9.5,
            -9.0,
            -8.5,
            -8.0,
            -7.5,
            -7.0,
            -6.5,
            -6.0,
            -5.5,
            -5.0,
            -4.5,
            -4.0,
            -3.5,
            -3.0,
        ]
    )

    codaii_z6 = np.array(
        [
            -5.57999992,
            -5.57999992,
            -4.80000019,
            -4.40999985,
            -4.17000008,
            -3.79999995,
            -3.47000003,
            -3.21000004,
            -3.0,
            -2.70000005,
            -2.5,
            -2.32999992,
            -2.1500001,
            -1.98000002,
            -1.83000004,
            -1.67999995,
            -1.52999997,
            -1.40999997,
            -1.29999995,
            -1.17999995,
            -1.08000004,
            -0.98000002,
            -0.88999999,
            -0.81999999,
            -0.77999997,
            -0.75999999,
            -0.85000002,
            -0.93000001,
            -0.92000002,
            -0.95999998,
            -0.94,
            -0.93000001,
            -0.95999998,
            -1.02999997,
            -1.12,
            -1.12,
            -1.49000001,
            -3.07999992,
            0.0,
            0.0,
            0.0,
            0.0,
        ]
    )

    lines = []
    labels = []

    # contraints
    oesch18_zeds = oesch18_uvlfs[0]
    if np.any(np.isclose(oesch18_zeds, tgt_zed, atol=prec_zed)):

        # only 1 redshift here no need for extra args

        oesch = ax.errorbar(
            oesch18_uvlfs[1][0][:, 0] - 0.1,
            (oesch18_uvlfs[1][0][:, 1] * 1e-4),
            yerr=(
                [
                    (oesch18_uvlfs[1][0][:, 1] - oesch18_uvlfs[1][0][:, 2]) * 1e-4,
                    (oesch18_uvlfs[1][0][:, 1] + oesch18_uvlfs[1][0][:, 3]) * 1e-4,
                ]
            ),
            linestyle="none",
            elinewidth=1.0,
            drawstyle="steps-mid",
            zorder=10.0,
            linewidth=2,
            color=color,
            fmt="^",
            mec=color,
            mfc="none",
            mew=1.5,
            capsize=3,
            uplims=oesch18_uvlfs[1][1],
        )

        
        labels.append("Oesch+18")
        lines.append(oesch)

    atek18_zeds = atek18_uvlfs[0]
    if np.any(np.isclose(atek18_zeds, tgt_zed, atol=prec_zed)):

        # only 1 redshift here no need for extra args

        atek = ax.errorbar(
            atek18_uvlfs[1][0][:, 0] + 0.1,
            10 ** (atek18_uvlfs[1][0][:, 1]),
            yerr=[
                np.abs(
                    10 ** atek18_uvlfs[1][0][:, 1]
                    - 10 ** (atek18_uvlfs[1][0][:, 1] - atek18_uvlfs[1][0][:, 2])
                ),
                np.abs(
                    -(10 ** atek18_uvlfs[1][0][:, 1])
                    + 10 ** (atek18_uvlfs[1][0][:, 1] + atek18_uvlfs[1][0][:, 2])
                ),
            ],
            linestyle="none",
            elinewidth=1.0,
            drawstyle="steps-mid",
            zorder=10.0,
            linewidth=2,
            color=color,
            fmt="D",
            mec=color,
            mfc="none",
            mew=1.5,
            capsize=3,
        )

        
        labels.append("Atek+18")
        lines.append(atek)

    # bouwens17_zeds = bouwens17_uvlfs[0]
    # if np.any(np.isclose(bouwens17_zeds, tgt_zed, atol=prec_zed)):

    #     # only 1 redshift here no need for extra args

    #     bouwens17 = ax.errorbar(
    #         bouwens17_uvlfs[1][0][0],
    #         (bouwens17_uvlfs[1][0][1]),
    #         yerr=([-bouwens17_uvlfs[1][0][2], bouwens17_uvlfs[1][0][3]]),
    #         linestyle="none",
    #         elinewidth=1.0,
    #         drawstyle="steps-mid",
    #         zorder=10.0,
    #         linewidth=2,
    #         color=color,
    #         fmt="H",
    #         mec=color,
    #         mfc="none",
    #         mew=1.5,
    #         capsize=3,
    #     )

        
    #     labels.append("Bouwens+17")
    #     lines.append(bouwens17)

    # ono18_zeds = ono18_uvlfs[0]
    # if np.any(np.isclose(ono18_zeds, tgt_zed, atol=prec_zed)):

    #     ono_z_arg = np.argmin(np.abs(ono18_zeds - tgt_zed))

    #     ono_err_switch = np.int8(ono18_uvlfs[1][ono_z_arg][3] != 0)

    #     print([10 ** tab for tab in ono18_uvlfs[1][ono_z_arg]])

    #     ono = ax.errorbar(
    #         ono18_uvlfs[1][ono_z_arg][0],
    #         10 ** (ono18_uvlfs[1][ono_z_arg][1]),
    #         yerr=(
    #             [
    #                 (
    #                     10 ** ono18_uvlfs[1][ono_z_arg][1]
    #                     - 10 ** ono18_uvlfs[1][ono_z_arg][2]
    #                 )
    #                 * ono_err_switch,
    #                 (
    #                     10 ** ono18_uvlfs[1][ono_z_arg][3]
    #                     + 10 ** ono18_uvlfs[1][ono_z_arg][1]
    #                 )
    #                 * ono_err_switch,
    #             ]
    #         ),
    #         linestyle="none",
    #         elinewidth=1.0,
    #         drawstyle="steps-mid",
    #         zorder=10.0,
    #         linewidth=2,
    #         color=color,
    #         fmt="X",
    #         mec=color,
    #         mfc="none",
    #         mew=1.5,
    #         capsize=3,
    #     )

    #     if not any(["Ono+18" in obs_label for obs_label in labels]):
    #         labels.append("Ono+18")
    #         lines.append(ono)

    bouwens21_zeds = bouwens21_uvlfs[0]
    if np.any(np.isclose(bouwens21_zeds, tgt_zed, atol=prec_zed)):

        # only 1 redshift here no need for extra args
        bouwens_z_arg = np.argmin(np.abs(bouwens21_zeds - tgt_zed))

        bouwens21 = ax.errorbar(
            bouwens21_uvlfs[1][bouwens_z_arg][0],
            (bouwens21_uvlfs[1][bouwens_z_arg][1]),
            yerr=bouwens21_uvlfs[1][bouwens_z_arg][2],
            linestyle="none",
            elinewidth=1.0,
            drawstyle="steps-mid",
            zorder=10.0,
            linewidth=2,
            color=color,
            fmt="o",
            mec=color,
            mfc="none",
            mew=1.5,
            capsize=3,
            label="Bouwens+21",
            uplims=bouwens21_uvlfs[1][bouwens_z_arg][3] == 1,
        )

    
        labels.append("Bouwens+21")
        lines.append(bouwens21)

    ishigaki18_zeds = ishigaki18_uvlfs[0]
    if np.any(np.isclose(ishigaki18_zeds, tgt_zed, atol=prec_zed)):

        ishigaki_z_arg = np.argmin(np.abs(ishigaki18_zeds - tgt_zed))

        ishigaki = ax.errorbar(
            ishigaki18_uvlfs[1][ishigaki_z_arg][0][0, :],
            10 ** (ishigaki18_uvlfs[1][ishigaki_z_arg][0][1, :]),
            yerr=(
                [
                    np.abs(
                        10 ** ishigaki18_uvlfs[1][ishigaki_z_arg][0][1, :]
                        - 10 ** ishigaki18_uvlfs[1][ishigaki_z_arg][1][1, :]
                    ),
                    np.abs(
                        10 ** ishigaki18_uvlfs[1][ishigaki_z_arg][0][1, :]
                        - 10 ** ishigaki18_uvlfs[1][ishigaki_z_arg][2][1, :]
                    ),
                ]
            ),
            linestyle="none",
            elinewidth=1.0,
            drawstyle="steps-mid",
            zorder=10.0,
            linewidth=2,
            color=color,
            fmt="s",
            mec=color,
            mfc="none",
            mew=1.5,
            capsize=3,
            uplims=ishigaki18_uvlfs[1][ishigaki_z_arg][-1],
        )

    
        labels.append("Ishigaki+18")
        lines.append(ishigaki)

    bowler20_zeds = bowler20_uvlfs[0]
    if np.any(np.isclose(bowler20_zeds, tgt_zed, atol=prec_zed)):

        bowler_z_arg = np.argmin(np.abs(bowler20_zeds - tgt_zed))

        bowler = ax.errorbar(
            bowler20_uvlfs[1][bowler_z_arg][:, 0],
            1e-6 * (bowler20_uvlfs[1][bowler_z_arg][:, 1]),
            yerr=1e-6
            * np.abs(
                bowler20_uvlfs[1][bowler_z_arg][:, 1]
                - bowler20_uvlfs[1][bowler_z_arg][:, 2]
            ),
            linestyle="none",
            elinewidth=1.0,
            drawstyle="steps-mid",
            zorder=10.0,
            linewidth=2,
            color=color,
            fmt="P",
            mec=color,
            mfc="none",
            mew=1.5,
            capsize=3,
        )

    
        labels.append("Bowler+20")
        lines.append(bowler)


    if np.abs(tgt_zed-donnan22e_uvlfs[0])<prec_zed:
        d22b = ax.errorbar(donnan22e_uvlfs[1], donnan22e_uvlfs[3], xerr=donnan22e_uvlfs[2], yerr=[donnan22e_uvlfs[-2:]],
        linestyle="none",
        elinewidth=1.0,
        drawstyle="steps-mid",
        zorder=10.0,
        linewidth=2,
        color=color,
        fmt="d",
        mec=color,
        mfc="none",
        mew=1.5,
        capsize=3,)
        lines.append(d22b)
        labels.append("Donnan+22e")

    if np.any(np.abs(tgt_zed - donnan22b_uvlfs[0])<prec_zed):

        donnan_whs = np.where(np.abs(tgt_zed - donnan22b_uvlfs[0])<prec_zed)[0]

        d22e_zeds, d22_mags, d22_mag_err, d22_uvlf, d22_errlow, d22_errhigh = [field[donnan_whs] for field in donnan22b_uvlfs]

        d22e = ax.errorbar(d22_mags, d22_uvlf*1e-6, xerr = d22_mag_err, yerr=[d22_errlow*1e-6, d22_errhigh*1e-6],
        linestyle="none",
        elinewidth=1.0,
        drawstyle="steps-mid",
        zorder=10.0,
        linewidth=2,
        color=color,
        fmt="H",
        mec=color,
        mfc="none",
        mew=1.5,
        capsize=3,)
        lines.append(d22e)
        labels.append("Donnan+22b")

    if 10<tgt_zed<13:

        # print(naidu22e_uvlfs)

        ndu22e = ax.errorbar(naidu22e_uvlfs[1], 10**naidu22e_uvlfs[2], yerr=[[10**(naidu22e_uvlfs[2]-naidu22e_uvlfs[3])], [10**(naidu22e_uvlfs[4]+naidu22e_uvlfs[2])]],
        linestyle="none",
        elinewidth=1.0,
        drawstyle="steps-mid",
        zorder=10.0,
        linewidth=2,
        color=color,
        fmt="<",
        mec=color,
        mfc="none",
        mew=1.5,
        capsize=3)
        labels.append('Naidu+22e')
        lines.append(ndu22e)
    

    harikane23_zeds = [z[0] for z in harikane23_uvlfs]
    if np.any(np.abs(harikane23_zeds-tgt_zed)<prec_zed):

        harikane23_uvlf = harikane23_uvlfs[np.argmin(np.abs(harikane23_zeds-tgt_zed))][1:]

        harikane23 = ax.errorbar(harikane23_uvlf[0], np.asarray(harikane23_uvlf[1])*1E-5, yerr=[np.asarray(harikane23_uvlf[2])*1e-5, np.asarray(harikane23_uvlf[3])*1e-5],
        uplims = harikane23_uvlf[-1],
        linestyle="none",
        elinewidth=1.0,
        drawstyle="steps-mid",
        zorder=10.0,
        linewidth=2,
        color=color,
        fmt=">",
        mec=color,
        mfc="none",
        mew=1.5,
        capsize=3)
        lines.append(harikane23)
        labels.append('Harikane+23')

    harikane22a_zeds = [z[0] for z in harikane22a_uvlfs]
    if np.any(np.abs(harikane22a_zeds-tgt_zed)<prec_zed):

        harikane22a_uvlf = harikane22a_uvlfs[np.argmin(np.abs(harikane22a_zeds-tgt_zed))]

        print(harikane22a_uvlf[3:])

        harikane22a = ax.errorbar(harikane22a_uvlf[1], harikane22a_uvlf[2], yerr=[harikane22a_uvlf[3], harikane22a_uvlf[4]],
        linestyle="none",
        elinewidth=1.0,
        drawstyle="steps-mid",
        zorder=10.0,
        linewidth=2,
        color=color,
        fmt="^",
        mec=color,
        mfc="none",
        mew=1.5,
        capsize=3)
        lines.append(harikane22a)
        labels.append('Harikane+22a')

    bouwens22e_uvlfs_z_bools = np.where([z[0]-0.5<=tgt_zed<=z[0]+0.5 for z in bouwens22e_uvlfs])[0]
    # print(bouwens22e_uvlfs, bouwens22e_uvlfs_z_bools)
    if len(bouwens22e_uvlfs_z_bools)>0:


        # print(bouwens22e_uvlfs)
        # print(bouwens22e_uvlfs_z_bools)
        # print(bouwens22e_uvlfs[bouwens22e_uvlfs_z_bools[0]])
        bouwens22e_uvlf = np.asarray(bouwens22e_uvlfs[bouwens22e_uvlfs_z_bools[0]][1:])

        # print(bouwens22e_uvlf)

        bouwens22e_uvlfs = ax.errorbar(bouwens22e_uvlf[0], bouwens22e_uvlf[1], yerr=bouwens22e_uvlf[2],
        linestyle="none",
        elinewidth=1.0,
        drawstyle="steps-mid",
        zorder=10.0,
        linewidth=2,
        color=color,
        fmt="*",
        mec=color,
        mfc="none",
        mew=1.5,
        capsize=3)
        lines.append(bouwens22e_uvlfs)
        labels.append('Bouwens+22e')


    bouwens22d_zeds, bouwens22d_uvlfs = bouwens22d_uvlfs



    if np.any(np.abs(bouwens22d_zeds - tgt_zed)<prec_zed):

        bouwens22d_uvlf = np.asarray(bouwens22d_uvlfs)[np.where(np.abs(bouwens22d_zeds - tgt_zed)<prec_zed)[0]]

        # print(bouwens22d_uvlfs)
        # print(tgt_zed,bouwens22d_uvlf)  

        bouw22d = ax.errorbar(bouwens22d_uvlf[:,0], bouwens22d_uvlf[:,1], yerr=np.abs(bouwens22d_uvlf[:,2]),
        linestyle="none",
        elinewidth=1.0,
        drawstyle="steps-mid",
        zorder=10.0,
        linewidth=2,
        color=color,
        fmt="3",
        mec=color,
        mfc="none",
        mew=1.5,
        capsize=3)
        lines.append(bouw22d)
        labels.append('Bouwens+22d')


    # print(tgt_zed, 10<=tgt_zed<=13)
    if np.abs(tgt_zed-11.)<prec_zed:

        # print(finkelstein23a_uvlfs)

        fink23a = ax.errorbar(finkelstein23a_uvlfs[1][0], finkelstein23a_uvlfs[1][1], yerr=[finkelstein23a_uvlfs[1][2], finkelstein23a_uvlfs[1][3]],
        uplims = finkelstein23a_uvlfs[1][-1],
        linestyle="none",
        elinewidth=1.0,
        drawstyle="steps-mid",
        zorder=10.0,
        linewidth=2,
        color=color,
        fmt="4",
        mec=color,
        mfc="none",
        mew=1.5,
        capsize=3)

        lines.append(fink23a)
        labels.append('Finkelstein+23a')

    return (lines, labels)
