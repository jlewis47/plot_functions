import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.colors import LogNorm
import matplotlib


def setup_plotting(scale_up=1.5):

    plt.rcParams["ytick.major.size"] = 15 * scale_up
    plt.rcParams["ytick.major.width"] = 1.5 * scale_up
    plt.rcParams["ytick.minor.size"] = 10 * scale_up
    plt.rcParams["ytick.minor.width"] = 1 * scale_up
    plt.rcParams["xtick.major.size"] = 15 * scale_up
    plt.rcParams["xtick.major.width"] = 1.5 * scale_up
    plt.rcParams["xtick.minor.size"] = 10 * scale_up
    plt.rcParams["xtick.minor.width"] = 1 * scale_up
    plt.rcParams["axes.linewidth"] = 1.75 * scale_up
    plt.rcParams["font.size"] = 16 * scale_up
    # plt.rcParams['figure.dpi']= 200
    plt.rcParams["figure.figsize"] = (10, 10)


def make_figure(*args, **kwargs):

    fig = plt.figure(*args, **kwargs)
    ax = fig.add_subplot(111)

    return (fig, ax)


def xy_plot(
    fig, ax, xs, ys, xlabel=None, ylabel=None, xscale="linear", yscale="linear", plot_args={}
):
    """quick wrapper for a simple 2d plot

    Args:
        fig: active pyplot figure
        ax: pyplot axis to draw on
        xs (_type_): _descriptfiles._
        ys (_type_): _descriptfiles._
        labels (_type_, optfiles.al): _descriptfiles._. Defaults to None.
        legend (_type_, optfiles.al): _descriptfiles._. Defaults to False.
        xlabel (_type_, optfiles.al): _descriptfiles._. Defaults to None.
        ylabel (_type_, optfiles.al): _descriptfiles._. Defaults to None.
        xscale (_type_, optfiles.al): _descriptfiles._. Defaults to 'linear'.
        yscale (_type_, optfiles.al): _descriptfiles._. Defaults to 'linear'.
    """

    # fig, ax = make_figure()

    plots = [ax.plot(x, y, **plot_args) for x, y in zip(xs, ys)]

    ax.grid()

    ax.set_xscale(xscale)
    ax.set_yscale(yscale)

    if xlabel != None:
        ax.set_xlabel(xlabel)
    if ylabel != None:
        ax.set_ylabel(ylabel)

    return [plot[0] for plot in plots]


def mf_plot(fig, ax, bins, mfs, xlabel=None, ylabel=None, xscale="log", yscale="log", plot_args={}):
    """quick wrapper for a simple 2d plot

    Args:
        fig: active pyplot figure
        ax: pyplot axis to draw on
        bins (_type_): _description_
        mfs (_type_): _description_
        labels (_type_, optional): _description_. Defaults to None.
        legend (_type_, optional): _description_. Defaults to False.
        xlabel (_type_, optional): _description_. Defaults to None.
        ylabel (_type_, optional): _description_. Defaults to None.
        xscale (_type_, optional): _description_. Defaults to 'linear'.
        yscale (_type_, optional): _description_. Defaults to 'linear'.
    """

    plots = [ax.plot(bin, mf, **plot_args) for bin, mf in zip(bins, mfs)]

    ax.grid()

    ax.set_xscale(xscale)
    ax.set_yscale(yscale)

    if xlabel != None:
        ax.set_xlabel(xlabel)
    if ylabel != None:
        ax.set_ylabel(ylabel)

    return [plot[0] for plot in plots]


def density_plot_fancy(
    stat,
    nbs,
    binsx,
    binsy,
    xlabel="",
    ylabel="",
    cax_label="Counts",
    xlog=True,
    ylog=True,
    collog=True,
    xhist_log=True,
    yhist_log=True,
    **kwargs
):

    """
    UPDATE
    """

    vmin = np.nanmin(stat)
    vmax = np.nanmax(stat)

    cmap = "jet"

    for key, value in kwargs.items():
        if key == "vmin":
            vmin = value
        if key == "vmax":
            vmax = value
        if key == "cmap":
            cmap = value

    if collog and vmin <= 0:
        vmin = np.nanmin(stat[stat != 0])

    current_cmap = matplotlib.cm.get_cmap()
    current_cmap.set_bad(color="white")

    print("Found (vmin,vmax)=(%.1e,%.1e)" % (vmin, vmax))

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)

    hist_1d_ticks = [0.0, 0.5, 1.0]

    divider = make_axes_locatable(ax)
    hist_x_ax = divider.append_axes("top", size="22%", pad=0.125)
    hist_x_ax.xaxis.set_tick_params(
        bottom=False, top=True, labelbottom=False, labeltop=True
    )

    x_axis_plot = np.sum(nbs, axis=1) / np.sum(nbs)
    hist_x_ax.plot((binsx[:-1]), x_axis_plot, drawstyle="steps-post")
    x_axis_ticks = (
        np.round(100 * np.asarray(hist_1d_ticks) * 1.1 * np.max(x_axis_plot)) / 100
    )

    hist_x_ax.set_xlim((binsx[0]), (binsx[-1]))
    hist_x_ax.set_xlabel(xlabel)
    hist_x_ax.set_ylabel("PDF")
    hist_x_ax.xaxis.set_label_position("top")
    hist_x_ax.set_yticks(x_axis_ticks)
    if xlog:
        hist_x_ax.set_xscale("log")
    hist_x_ax.xaxis.set_tick_params(bottom=False, labelbottom=False, which="both")
    hist_x_ax.grid()

    hist_y_ax = divider.append_axes("left", size="22%", pad=0.125)
    hist_y_ax.xaxis.set_tick_params(left=True, labelleft=True, which="both")

    y_axis_plot = np.sum(nbs, axis=0) / np.sum(nbs)
    hist_y_ax.plot(y_axis_plot, (binsy[:-1]), drawstyle="steps-pre")
    y_axis_ticks = (
        np.round(100 * np.asarray(hist_1d_ticks) * 1.1 * np.max(y_axis_plot)) / 100
    )

    hist_y_ax.set_ylim((binsy[0]), (binsy[-1]))
    hist_y_ax.invert_xaxis()
    hist_y_ax.set_ylabel(ylabel)
    hist_y_ax.set_xlabel("PDF")
    hist_y_ax.set_xticks(y_axis_ticks)
    hist_y_ax.set_xticklabels(map(str, y_axis_ticks), rotation=45)
    if ylog:
        hist_y_ax.set_yscale("log")
    hist_y_ax.grid()

    hist_x_ax.xaxis.set_tick_params(
        bottom=False, top=False, labelbottom=False, labeltop=False, which="minor"
    )

    ax.yaxis.set_tick_params(left=False, labelleft=False, which="both")
    ax.xaxis.set_tick_params(bottom=False, labelbottom=False, which="both")

    cax = divider.append_axes("right", size="5%", pad=0.125)

    if yhist_log:
        # hist_y_ax.set_xlim(1e-2,1)
        hist_y_ax.set_xscale("log")
    if xhist_log:
        # hist_x_ax.set_ylim(1e-2,1)
        hist_x_ax.set_yscale("log")

    if collog:
        if xlog and ylog:
            img = ax.imshow(
                (stat.T),
                extent=np.log10([binsx[0], binsx[-1], binsy[0], binsy[-1]]),
                aspect="auto",
                origin="lower",
                norm=LogNorm(),
                vmin=vmin,
                vmax=vmax,
                cmap=cmap,
            )
        elif xlog:
            img = ax.imshow(
                (stat.T),
                extent=[np.log10(binsx[0]), np.log10(binsx[-1]), binsy[0], binsy[-1]],
                aspect="auto",
                origin="lower",
                norm=LogNorm(),
                vmin=vmin,
                vmax=vmax,
                cmap=cmap,
            )
        elif ylog:
            img = ax.imshow(
                (stat.T),
                extent=[binsx[0], binsx[-1], np.log10(binsy[0]), np.log10(binsy[-1])],
                aspect="auto",
                origin="lower",
                norm=LogNorm(),
                vmin=vmin,
                vmax=vmax,
                cmap=cmap,
            )
        else:
            img = ax.imshow(
                (stat.T),
                extent=[binsx[0], binsx[-1], binsy[0], binsy[-1]],
                aspect="auto",
                origin="lower",
                norm=LogNorm(),
                vmin=vmin,
                vmax=vmax,
                cmap=cmap,
            )
    else:
        if xlog and ylog:
            img = ax.imshow(
                (stat.T),
                extent=np.log10([binsx[0], binsx[-1], binsy[0], binsy[-1]]),
                aspect="auto",
                origin="lower",
                vmin=vmin,
                vmax=vmax,
                cmap=cmap,
            )
        elif xlog:
            img = ax.imshow(
                (stat.T),
                extent=[np.log10(binsx[0]), np.log10(binsx[-1]), binsy[0], binsy[-1]],
                aspect="auto",
                origin="lower",
                vmin=vmin,
                vmax=vmax,
                cmap=cmap,
            )
        elif ylog:
            img = ax.imshow(
                (stat.T),
                extent=[binsx[0], binsx[-1], np.log10(binsy[0]), np.log10(binsy[-1])],
                aspect="auto",
                origin="lower",
                vmin=vmin,
                vmax=vmax,
                cmap=cmap,
            )
        else:
            img = ax.imshow(
                (stat.T),
                extent=[binsx[0], binsx[-1], binsy[0], binsy[-1]],
                aspect="auto",
                origin="lower",
                vmin=vmin,
                vmax=vmax,
                cmap=cmap,
            )

    plt.colorbar(img, cax=cax)

    ax.grid()

    # cax.set_yscale('log')
    cax.set_ylabel(cax_label)
    cax.yaxis.set_label_position("right")
    cax.yaxis.set_tick_params(
        left=False, labelleft=False, right=True, labelright=True, which="both"
    )
    # cax.yaxis.set_tick_params(left=False,labelleft=False,right=False,labelright=False,which='minor')

    # cax_ticks=cax.get_yticklabels()
    # cax.set_yticklabels(["%.1e"%10**float(tick.get_text()) for tick in cax_ticks])

    return (fig, ax, hist_x_ax, hist_y_ax, cax)
    # plt.show()
