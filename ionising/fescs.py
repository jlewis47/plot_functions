import numpy as np
import matplotlib.pyplot as plt
import os

# from generic.stat import xy_stat
from ..generic.plot_functions import xy_plot_vect, density_plot_fancy
from ..utils.utils import get_mod_path
import h5py
import csv


def fesc_plot(
    fig, ax, masses, fescs, fesc_type, redshift, xlabel, log=True, **plot_args
):
    fesc_labels = {
        "gas": "$\mathrm{f_{esc, g}}$",
        "dust": "$\mathrm{f_{esc, d}}$",
        "full": "$\mathrm{f_{esc, gxd}}$",
    }

    # plot_args = {'ls':'-', 'lw':3}
    if log:
        lines = xy_plot_vect(
            fig,
            ax,
            masses,
            fescs,
            xlabel=xlabel,
            ylabel=fesc_labels[fesc_type],
            xscale="log",
            yscale="log",
            **plot_args,
        )
    else:
        lines = xy_plot_vect(
            fig,
            ax,
            masses,
            fescs,
            xlabel=xlabel,
            ylabel=fesc_labels[fesc_type],
            **plot_args,
        )
    # if not os.path.isdir('./figs'): os.makedirs('./figs')

    if redshift != None:
        ax.set_title(f"z={redshift:.1f}, star forming haloes")

    # fig.savefig(f'./figs/fesc_comparison_{fesc_type:s}_{out_nb:d}')
    return lines


def fesc_Mh_plot(
    fig, ax, masses, fescs, fesc_type, redshift=None, log=True, **plot_args
):
    return fesc_plot(
        fig,
        ax,
        masses,
        fescs,
        fesc_type,
        redshift,
        xlabel="$\mathrm{Halo \, \, masses, \, M_\odot}$",
        log=log,
        **plot_args,
    )


def fesc_Mst_plot(
    fig, ax, masses, fescs, fesc_type, redshift=None, log=True, **plot_args
):
    return fesc_plot(
        fig,
        ax,
        masses,
        fescs,
        fesc_type,
        redshift,
        xlabel="$\mathrm{Stellar \, \, masses, \, M_\odot}$",
        log=log,
        **plot_args,
    )


def plot_cosmic_fesc(fig, ax, redshifts, fescs, **plot_args):
    lines = xy_plot_vect(
        fig,
        ax,
        redshifts,
        fescs,
        xlabel="redshift",
        ylabel="$\mathrm{<f_{esc}>_{Lintr}}$",
        xscale="linear",
        yscale="log",
        **plot_args,
    )

    ax.invert_xaxis()

    return lines


def plot_fesc_density(fig, ax, nbs, binsx, binsy, fesc_type, cb=True, **kwargs):
    fesc_labels = {
        "gas": "$\mathrm{f_{esc, g}}$",
        "dust": "$\mathrm{f_{esc, d}}$",
        "full": "$\mathrm{f_{esc, gxd}}$",
    }

    density_plot_fancy(
        fig,
        ax,
        nbs,
        nbs,
        binsx,
        binsy,
        xlabel="$\mathrm{Halo \, \, masses, \, M_\odot}$",
        ylabel=fesc_labels[fesc_type],
        cb=cb,
        **kwargs,
    )


def plot_dustier_fesc(ax, redshift, fkey="fesc", zprec=0.1, **plot_args):
    dir_path = get_mod_path()

    assert (
        fkey == "fesc" or fkey == "fesc_total"
    ), "fkey must be either fesc or fesc_total"

    with h5py.File(
        os.path.join(dir_path, "../constraints/dustier_median_fescs")
    ) as src:
        redshifts = src["redshifts"][()]
        masses = src["mbins"][()]
        fescs = src[fkey][()]

    dist = np.abs(redshift - redshifts)

    if np.any(dist):
        whs = np.argmin(dist)

        (l,) = ax.plot(masses, fescs[whs], **plot_args)

    label = "DUSTiER"

    return ([l], [label])


def plot_dustier_fesc_ms(ax, redshift, fkey="fesc", zprec=0.1, **plot_args):
    dir_path = get_mod_path()

    assert (
        fkey == "fesc" or fkey == "fesc_total"
    ), "fkey must be either fesc or fesc_total"

    with h5py.File(
        os.path.join(dir_path, "../constraints/dustier_fesc_mstar.hdf5")
    ) as src:
        redshifts = src["redshifts"][()]
        masses = src["mass_bins"][()]
        fescs = src["median_fesc_gas"][()]

    dist = np.abs(redshift - redshifts)

    if np.any(dist):
        whs = np.argmin(dist)

        (l,) = ax.plot(masses / 0.8, fescs[whs], **plot_args)

    label = "DUSTiER"

    return ([l], [label])


def plot_cosmic_fesc_constraints(ax, redshifts, **plot_args):
    dir_path = get_mod_path()

    puch_fesc_avg = np.min(
        [6.9 * 10 ** (-5) * (1 + redshifts) ** 3.97, 0.18 * np.ones_like(redshifts)],
        axis=0,
    )

    dayal20_fesc = 0.02 * ((1 + redshifts) / 7.0) ** 2.8

    ferrera_2013 = (
        np.asarray(
            [
                6.132050010787905,
                0.09161999306050028,
                6.450907539223551,
                0.1047705478903892,
                6.727632192518877,
                0.1149836240346237,
                6.957680409194827,
                0.14561776942894866,
                7.174644400442444,
                0.1720573145375054,
                7.377104577173528,
                0.19830881593076122,
                7.55053022637645,
                0.22525517426244768,
                7.694932190855438,
                0.25246469102721847,
                7.826300177920929,
                0.2851486562388549,
                7.96535746239481,
                0.31655801853655774,
                8.102091537053237,
                0.34418981039701424,
                8.301176501319269,
                0.3764569721483487,
                8.477413583504328,
                0.40699754622736917,
                8.650774175881903,
                0.43653409559113365,
                8.850272283003394,
                0.4651888709616807,
                9.052645641476873,
                0.49489697926837384,
                9.259519594849168,
                0.523154672950499,
                9.515536231162347,
                0.5499446694296811,
                9.788496903736435,
                0.5749835720450176,
                10.074628097492672,
                0.5961647112371792,
                10.413289454719793,
                0.6206589728513482,
                10.732063829715113,
                0.6371202225124478,
                11.050863504586957,
                0.6525741756610726,
                11.369749871343396,
                0.6645765533473713,
                11.688749468316447,
                0.6720707508379786,
                12.007790642009661,
                0.6779096009129805,
                12.326773431372432,
                0.6860729814013857,
                12.645666875017408,
                0.6977935978254536,
                12.964631087547769,
                0.7066966016272145,
                13.283551954135831,
                0.7173253931601384,
                13.602566589497027,
                0.7242208479685055,
                13.921615724689845,
                0.7297427166234978,
                14.240634783106376,
                0.7364620706429705,
                14.559651187689706,
                0.7432870851357799,
                14.878614515608998,
                0.7522253090953196,
                15.197667189246086,
                0.7576062971191967,
                15.516701286050761,
                0.7637269084564291,
                15.835654883248312,
                0.7730525541515361,
                16.154670403220575,
                0.7799127888021242,
                16.473815961019728,
                0.7815956602592231,
                16.792943826597536,
                0.7839829348718987,
                17.11193988512632,
                0.7916180129936214,
                17.430943905154702,
                0.7989361096953346,
                17.75003019401235,
                0.8029787317236157,
                18.06910852137039,
                0.8073383351719063,
                18.38811431062091,
                0.8145859915580617,
                18.707178484201872,
                0.8195091175308138,
                19.026278042225524,
                0.8230234371924123,
                19.345329831251544,
                0.8284396453740681,
                19.664428504664134,
                0.8319891851934454,
                19.983505947411107,
                0.8363840087995149,
                20.302528544271905,
                0.8429624821878724,
                20.476604963925126,
                0.8439988798770006,
            ]
        )
        .reshape((-1, 2))
        .T
    )

    fink_2019 = (
        np.asarray(
            [
                4.200000000000001,
                0.007665902203754904,
                4.4,
                0.008190715261573056,
                4.600000000000001,
                0.00879806235531369,
                4.800000000000002,
                0.00941672301239474,
                5.000000000000002,
                0.010220264380531613,
                5.200000000000001,
                0.010997644391888745,
                5.400000000000001,
                0.011769905021379284,
                5.600000000000002,
                0.012692574725293532,
                5.8000000000000025,
                0.01416070990317847,
                6.000000000000003,
                0.015506416813799884,
                6.200000000000003,
                0.016813022576140202,
                6.400000000000003,
                0.01811893798169742,
                6.600000000000004,
                0.019276623907854173,
                6.800000000000003,
                0.02056613824712497,
                7.0000000000000036,
                0.02211553932789584,
                7.200000000000003,
                0.023625011352136016,
                7.400000000000003,
                0.025532877784970737,
                7.600000000000004,
                0.02759527592273503,
                7.800000000000004,
                0.029437734476380928,
                8.000000000000002,
                0.031272372643124796,
                8.200000000000003,
                0.03341479193888536,
                8.400000000000002,
                0.036562682844480277,
                8.600000000000001,
                0.03973732437631666,
                8.799999999999999,
                0.04239603485439379,
                8.999999999999998,
                0.04479830553745277,
                9.199999999999998,
                0.047543742220897245,
                9.399999999999999,
                0.05037520533578599,
                9.599999999999998,
                0.0530878993307992,
                9.799999999999995,
                0.05560339818358799,
                9.999999999999996,
                0.05816435023688141,
                10.199999999999996,
                0.060122280197774144,
                10.399999999999995,
                0.06186964193314319,
                10.599999999999996,
                0.06367931010265676,
                10.799999999999994,
                0.06511455940421244,
                10.999999999999993,
                0.06606343450102241,
                11.199999999999992,
                0.06712598717921207,
                11.399999999999991,
                0.06837363854137353,
                11.599999999999989,
                0.06969589222876713,
                11.799999999999988,
                0.07056046371603693,
                11.999999999999988,
                0.0715349375706614,
                12.199999999999987,
                0.07269194943529611,
                12.399999999999988,
                0.0739835612583989,
                12.599999999999989,
                0.07522719310357805,
                12.799999999999986,
                0.07598030686809952,
                12.999999999999986,
                0.07707496468396736,
                13.199999999999985,
                0.0787229390904307,
                13.399999999999984,
                0.08154318792970379,
                13.599999999999982,
                0.08473610449052482,
                13.799999999999983,
                0.08750406278813376,
                13.999999999999982,
                0.08994600445346346,
                14.19999999999998,
                0.09259838553107277,
                14.39999999999998,
                0.09516125165439478,
                14.599999999999978,
                0.09746856603969435,
                14.79999999999998,
                0.10082205223973509,
            ]
        )
        .reshape((-1, 2))
        .T
    )

    # line_coda2=ax.plot(codaii_reds,codaii_SFRavg_fescs,linewidth=2,label='CoDa II',color='indigo')[0]

    # line_kimm=ax.plot(kimm[:,0],kimm[:,1],linewidth=2,label='Kimm+14')[0]

    # line_katz=ax.plot(katz[:,0],katz[:,1],linewidth=2,label='Katz+18')[0]

    line_ferr = ax.plot(
        ferrera_2013[0],
        ferrera_2013[1],
        linewidth=2,
        label=r"Ferrara+13, $\mathrm{f_\star=0.03}$",
        linestyle="dashdot",
    )[0]

    line_puch = ax.plot(
        redshifts,
        puch_fesc_avg,
        linewidth=2,
        label=r"Puchwein+19, fiducial",
        linestyle="dashdot",
    )[0]

    # line_sphx=ax.plot(sphinx_zeds,sphinx_data[1],linewidth=2,label=r'Rosdahl+18')[0]

    line_fink = ax.plot(
        fink_2019[0],
        fink_2019[1],
        linewidth=2,
        label=r"Finkelstein+19",
        linestyle="dashdot",
    )[0]

    line_daya = ax.plot(
        redshifts,
        dayal20_fesc,
        linewidth=2,
        label=r"Dayal+20, fiducial",
        linestyle="dashdot",
    )[0]

    return (
        [line_ferr, line_fink, line_puch, line_daya],
        ["Ferrara+13", "Finkelstein+19", "Puchwein+19", "Dayal+20"],
    )


def plot_Mh_fesc_constraints(ax, redshift, zprec=0.5, log=False, **plot_args):
    if log == True:
        scale_fct = lambda x: np.log10(x)
    else:
        scale_fct = lambda x: x

    dir_path = get_mod_path()

    labels = []
    lines = []

    kimm_2014_z7 = (
        np.asarray(
            [
                8.241087147887324,
                52.92275951740657,
                8.297687164654594,
                49.05903109968728,
                8.354287181421864,
                45.52459194052973,
                8.410887198189135,
                42.24479010073551,
                8.467487214956405,
                39.133549023957364,
                8.524087231723675,
                36.31418743024728,
                8.580687248490946,
                33.6591193201515,
                8.637287265258216,
                31.270190040083,
                8.692172130002236,
                29.728272938190095,
                8.750487298792756,
                28.80542717200129,
                8.807087315560027,
                28.056264846644197,
                8.863687332327297,
                27.358108160408907,
                8.920287349094567,
                26.64658724442178,
                8.976887365861838,
                25.953571336563094,
                9.033487382629108,
                25.293154590100684,
                9.090087399396378,
                24.692205637904554,
                9.146687416163648,
                23.925574277576256,
                9.203287432930919,
                22.278784722406336,
                9.259887449698189,
                20.578602746177648,
                9.316487466465459,
                19.052046125216936,
                9.37308748323273,
                17.60825623273317,
                9.4296875,
                16.302045093561237,
                9.48628751676727,
                15.09273097346635,
                9.54288753353454,
                13.965073733394956,
                9.599487550301811,
                12.906781507376285,
                9.656087567069081,
                12.080923415569558,
                9.712687583836352,
                11.746396277232485,
                9.769287600603622,
                11.701010899377925,
                9.825887617370892,
                11.669246037498874,
                9.882487634138162,
                11.671156759616322,
                9.939087650905432,
                11.673067794595383,
                9.995687667672703,
                11.561131955472748,
                10.04199677230047,
                11.592235023042054,
            ]
        )
        .reshape((-1, 2))
        .T
    )

    yajima_2011_z6 = (
        np.asarray(
            [
                10.99789143615915,
                0.030273743055935335,
                10.4995056553666,
                0.12805105858419752,
                9.994218247556272,
                0.11372840351090967,
                9.500046394803782,
                0.2075821829492497,
                9.005672964627962,
                0.31644567655410455,
            ]
        )
        .reshape((-1, 2))
        .T
    )

    kostyuk22 = np.asarray(
        [
            [8.265e8, 3.867e-1],
            [9.144e8, 3.565e-1],
            [1.012e9, 3.473e-1],
            [1.119e9, 3.513e-1],
            [1.238e9, 3.496e-1],
            [1.370e9, 3.397e-1],
            [1.516e9, 3.418e-1],
            [1.677e9, 3.546e-1],
            [1.855e9, 3.505e-1],
            [2.053e9, 3.395e-1],
            [2.230e9, 3.533e-1],
            [2.392e9, 3.785e-1],
            [2.571e9, 4.102e-1],
            [2.832e9, 4.254e-1],
            [3.133e9, 4.364e-1],
            [3.466e9, 4.548e-1],
            [3.835e9, 4.737e-1],
            [4.243e9, 4.918e-1],
            [4.694e9, 5.093e-1],
            [5.193e9, 5.266e-1],
            [5.746e9, 5.409e-1],
            [6.357e9, 5.486e-1],
            [7.033e9, 5.548e-1],
            [7.781e9, 5.588e-1],
            [8.609e9, 5.621e-1],
            [9.524e9, 5.660e-1],
            [1.054e10, 5.668e-1],
            [1.166e10, 5.642e-1],
            [1.290e10, 5.644e-1],
            [1.427e10, 5.694e-1],
            [1.579e10, 5.710e-1],
            [1.747e10, 5.697e-1],
            [1.933e10, 5.697e-1],
            [2.138e10, 5.699e-1],
            [2.366e10, 5.695e-1],
            [2.617e10, 5.667e-1],
            [2.896e10, 5.733e-1],
            [3.204e10, 5.848e-1],
            [3.544e10, 5.922e-1],
            [3.921e10, 5.955e-1],
            [4.339e10, 5.894e-1],
            [4.800e10, 5.785e-1],
            [5.262e10, 5.690e-1],
        ]
    )

    codaii_z, codaii_m, codaii_fesc = codaii_fesc_mh()

    sphx_z, sphx_mfesc = sphinx22_fesc_mh()

    (l,) = ax.plot(
        scale_fct(kostyuk22[:, 0]),
        scale_fct(kostyuk22[:, 1] * 0.3),
        **plot_args,
        marker="v",
        c="k",
        markevery=5,
    )
    lines.append(l)
    labels.append("Kostyuk+22")

    if np.abs(redshift - 7) < zprec:
        (l,) = ax.plot(
            scale_fct(10 ** kimm_2014_z7[0]),
            scale_fct(kimm_2014_z7[1] / 100.0),
            **plot_args,
            marker="D",
            c="k",
            markevery=4,
        )
        lines.append(l)
        labels.append("Kimm+14")

    if np.abs(redshift - 6) < zprec:
        (l,) = ax.plot(
            scale_fct(10 ** yajima_2011_z6[0]),
            scale_fct(yajima_2011_z6[1]),
            **plot_args,
            marker="o",
            c="k",
        )
        lines.append(l)
        labels.append("Yajima+11")

    if np.any(np.abs(codaii_z - np.asarray(redshift)) <= zprec):
        coda_z_arg = np.argmin(np.abs(codaii_z - np.asarray(redshift)))

        (l,) = ax.plot(
            scale_fct(codaii_m[:-1] + np.diff(codaii_m) * 0.5),
            scale_fct(codaii_fesc[coda_z_arg] * 0.42),
            **plot_args,
            marker="X",
            c="k",
            markevery=2,
        )
        lines.append(l)
        labels.append("CoDa II (Lewis+20)")

    if np.any(np.abs(np.asarray(sphx_z) - redshift) <= zprec):
        sphx_z_arg = np.argmin(np.abs(np.asarray(sphx_z) - redshift))

        (l,) = ax.plot(
            scale_fct(sphx_mfesc[sphx_z_arg][0, :]),
            scale_fct(sphx_mfesc[sphx_z_arg][1, :]),
            **plot_args,
            marker="s",
            c="k",
        )
        lines.append(l)
        labels.append("Sphinx (Rosdahl+22)")

    return (lines, labels)


def plot_Mst_fesc_constraints(ax, redshift, zprec=0.5, **plot_args):
    dir_path = get_mod_path()

    pass


def codaii_fesc_mh():
    dir_path = get_mod_path()

    with open(os.path.join(dir_path, "../constraints/codaii_fesc_z60"), "r") as src:
        reader = csv.reader(src, delimiter=",")

        read_ins = []
        for line in reader:
            read_ins.append(np.float64(line))

    codaii_avg_fesc_bins = read_ins[1]
    codaii_avg_fescs_z6 = read_ins[0]

    with open(os.path.join(dir_path, "../constraints/codaii_fesc_z101"), "r") as src:
        reader = csv.reader(src, delimiter=",")

        read_ins = []
        for line in reader:
            read_ins.append(np.float64(line))

    codaii_avg_fesc_bins = read_ins[1]
    codaii_avg_fescs_z10 = read_ins[0]

    codaii_redshifts = [6, 10.1]
    codaii_fescs = [codaii_avg_fescs_z6, codaii_avg_fescs_z10]

    return (codaii_redshifts, codaii_avg_fesc_bins, codaii_fescs)


def sphinx22_fesc_mh():
    data65 = (
        np.asarray(
            [
                1.616e7,
                9.848e-3,
                2.317e7,
                1.634e-2,
                3.194e7,
                2.424e-2,
                4.681e7,
                3.682e-2,
                6.709e7,
                5.050e-2,
                9.282e7,
                3.756e-2,
                1.220e8,
                2.567e-2,
                1.392e8,
                1.940e-2,
                2.003e8,
                2.184e-2,
                2.920e8,
                2.514e-2,
                4.256e8,
                2.745e-2,
                6.202e8,
                2.923e-2,
                9.040e8,
                3.250e-2,
                1.318e9,
                3.668e-2,
                1.920e9,
                3.560e-2,
                2.797e9,
                3.181e-2,
                3.999e9,
                3.081e-2,
                5.864e9,
                3.144e-2,
                8.655e9,
                2.962e-2,
                1.240e10,
                2.693e-2,
                1.900e10,
                1.880e-2,
                2.629e10,
                1.271e-2,
                3.575e10,
                8.582e-3,
                4.780e10,
                5.693e-3,
                6.500e10,
                3.736e-3,
            ]
        )
        .reshape((-1, 2))
        .T
    )

    data76 = (
        np.asarray(
            [
                1.642e7,
                2.500e-2,
                2.391e7,
                3.147e-2,
                3.483e7,
                3.757e-2,
                5.073e7,
                3.819e-2,
                7.389e7,
                3.782e-2,
                1.076e8,
                3.435e-2,
                1.568e8,
                3.138e-2,
                2.283e8,
                3.121e-2,
                3.325e8,
                3.555e-2,
                4.843e8,
                4.063e-2,
                7.054e8,
                4.929e-2,
                1.027e9,
                5.232e-2,
                1.497e9,
                5.471e-2,
                2.155e9,
                5.471e-2,
                3.216e9,
                5.409e-2,
                4.624e9,
                4.986e-2,
                6.916e9,
                4.486e-2,
                9.809e9,
                3.889e-2,
                1.429e10,
                3.162e-2,
                1.910e10,
                1.985e-2,
                2.345e10,
                1.325e-2,
                3.136e10,
                8.449e-3,
                4.568e10,
                9.954e-3,
                6.321e10,
                1.294e-2,
            ]
        )
        .reshape((-1, 2))
        .T
    )

    data87 = (
        np.asarray(
            [
                1.470e7,
                1.691e-1,
                1.744e7,
                1.128e-1,
                2.035e7,
                7.571e-2,
                2.333e7,
                5.118e-2,
                2.675e7,
                3.507e-2,
                3.457e7,
                2.457e-2,
                5.026e7,
                3.063e-2,
                7.309e7,
                3.772e-2,
                1.063e8,
                3.687e-2,
                1.547e8,
                3.805e-2,
                2.249e8,
                4.497e-2,
                3.271e8,
                5.229e-2,
                4.758e8,
                5.569e-2,
                6.921e8,
                5.785e-2,
                1.007e9,
                5.901e-2,
                1.465e9,
                5.920e-2,
                2.114e9,
                6.017e-2,
                3.275e9,
                6.325e-2,
                5.345e9,
                6.586e-2,
                7.776e9,
                5.690e-2,
                1.113e10,
                3.789e-2,
                1.592e10,
                2.764e-2,
                2.317e10,
                2.393e-2,
                3.043e10,
                2.166e-2,
            ]
        )
        .reshape((-1, 2))
        .T
    )

    data98 = (
        np.asarray(
            [
                1.614e7,
                6.871e-2,
                2.272e7,
                1.037e-1,
                3.253e7,
                1.262e-1,
                4.501e7,
                8.917e-2,
                6.228e7,
                5.757e-2,
                9.071e7,
                5.060e-2,
                1.321e8,
                4.945e-2,
                1.924e8,
                5.179e-2,
                2.803e8,
                5.634e-2,
                4.082e8,
                6.000e-2,
                5.946e8,
                6.232e-2,
                8.660e8,
                6.702e-2,
                1.219e9,
                7.137e-2,
                2.062e9,
                7.351e-2,
                2.965e9,
                7.401e-2,
                4.318e9,
                7.401e-2,
                6.290e9,
                7.389e-2,
                9.161e9,
                6.263e-2,
                1.312e10,
                5.006e-2,
            ]
        )
        .reshape((-1, 2))
        .T
    )

    return ([5.5, 6.5, 7.5, 8.5], [data65, data76, data87, data98])
