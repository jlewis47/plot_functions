import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.colors import LogNorm
import matplotlib
from ..utils.utils import is_iter


def get_fig_sizes(keys):

    if type(keys[0])==str:
        keys = list(keys)

    figs_sizes={"a4":(11.7,8.3),
            "col_width":10./3,
            "page_width":20./3}

    return([figs_sizes[key] for key in keys])

def setup_plotting(scale_up=1):

    plt.rcParams['ytick.major.size']=10*scale_up
    plt.rcParams['ytick.major.width']=1.5*scale_up
    plt.rcParams['ytick.minor.size']=7*scale_up
    plt.rcParams['ytick.minor.width']=1*scale_up
    plt.rcParams['xtick.major.size']=10*scale_up
    plt.rcParams['xtick.major.width']=1.5*scale_up
    plt.rcParams['xtick.minor.size']=7*scale_up
    plt.rcParams['xtick.minor.width']=1*scale_up
    plt.rcParams['axes.linewidth']=1.75*scale_up
    plt.rcParams['font.size']= 10*scale_up
    plt.rcParams['legend.fontsize']= 10*scale_up
    plt.rcParams['legend.framealpha']= 0.0
    #plt.rcParams['figure.dpi']= 200 
    plt.rcParams['figure.figsize']= tuple(get_fig_sizes(["col_width","col_width"]))
    plt.rcParams["xtick.direction"]='in'
    plt.rcParams["xtick.top"]=True
    plt.rcParams["ytick.direction"]='in'
    plt.rcParams["ytick.right"]=True
    plt.rcParams["image.origin"]='lower'
    plt.rcParams["image.aspect"]='auto'
    plt.rcParams["markers.fillstyle"]='none'
    # plt.rcParams["savefig.fillstyle"]='empty'


def make_figure(*args, **kwargs):

    if "figsize_key" in kwargs:
        kwargs["figsize"]=get_fig_sizes(kwargs["figsize_key"])

    fig = plt.figure(*args, **kwargs)
    ax = fig.add_subplot(111)

    return (fig, ax)


def xy_plot(
    fig, ax, xs, ys, xlabel=None, ylabel=None, xscale="log", yscale="log", xerrs=[], yerrs=[], **plot_args
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

    ax.grid()

    ax.set_xscale(xscale)
    ax.set_yscale(yscale)

    if xlabel != None:
        ax.set_xlabel(xlabel)
    if ylabel != None:
        ax.set_ylabel(ylabel)


    if is_iter(xs[0]):
        if xerrs==[]:
            xerrs = [np.zeros_like(x) for x in xs]
        if yerrs==[]:
            yerrs = [np.zeros_like(x) for x in xs]

        plots = [ax.errorbar(x, y, xerr=xerr, yerr=yerr, **plot_args)[0] for x, y, xerr, yerr in zip(xs, ys, xerrs, yerrs)]

    else:
        if xerrs==[]:
            xerrs = np.zeros_like(xs)
        if yerrs==[]:
            yerrs = np.zeros_like(xs)

        plots = ax.errorbar(xs, ys, xerr=xerrs, yerr=yerrs, **plot_args)[0]

    return plots

    



def mf_plot(fig, ax, bins, mfs, xlabel=None, ylabel=None, xscale="log", yscale="log", xerrs=[], yerrs=[], **plot_args):
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




    if is_iter(bins[0]):
        if xerrs==[]:
            xerrs = [np.zeros_like(x) for x in bins]
        if yerrs==[]:
            yerrs = [np.zeros_like(x) for x in bins]

        plots = [ax.errorbar(bin, mf, xerr=xerr, yerr=yerr,  **plot_args)[0] for bin, mf, xerr, yerr in zip(bins, mfs, xerrs, yerrs)]

    else:
        if xerrs==[]:
            xerrs = np.zeros_like(bins)
        if yerrs==[]:
            yerrs = np.zeros_like(bins)
        
        plots = ax.errorbar(bins, mfs, xerr=xerrs, yerr=yerrs,  **plot_args)[0]

    ax.grid()

    ax.set_xscale(xscale)
    ax.set_yscale(yscale)

    if xlabel != None:
        ax.set_xlabel(xlabel)
    if ylabel != None:
        ax.set_ylabel(ylabel)

    return plots

def subplots_land():
    pass    

def subplots_port():
    pass

def mk_shared_colorbar():
    pass

def density_plot_fancy(
    fig,
    ax,
    stat,
    nbs,
    binsx,
    binsy,
    xlabel="",
    ylabel="",
    cax_label="Counts",
    cb=True,
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
    
    hist_1d_ticks = [0.0, 0.5, 1.0]

    divider = make_axes_locatable(ax)
    hist_x_ax = divider.append_axes("top", size="22%", pad=0.125)
    hist_x_ax.xaxis.set_tick_params(
        bottom=False, top=True, labelbottom=False, labeltop=True
    )

    x_axis_plot = np.sum(nbs, axis=1) / np.sum(nbs)
    hist_x_ax.plot((binsx), x_axis_plot, drawstyle="steps-post")
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
    hist_y_ax.plot(y_axis_plot, (binsy), drawstyle="steps-pre")
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
    if cb: cax = divider.append_axes("right", size="5%", pad=0.125)

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
                
                origin="lower",
                norm=LogNorm(vmin=vmin, vmax=vmax),
                cmap=cmap,
            )
        elif xlog:
            img = ax.imshow(
                (stat.T),
                extent=[np.log10(binsx[0]), np.log10(binsx[-1]), binsy[0], binsy[-1]],
                
                origin="lower",
                norm=LogNorm(vmin=vmin, vmax=vmax),
                cmap=cmap,
            )
        elif ylog:
            img = ax.imshow(
                (stat.T),
                extent=[binsx[0], binsx[-1], np.log10(binsy[0]), np.log10(binsy[-1])],
                
                origin="lower",
                norm=LogNorm(vmin=vmin, vmax=vmax),
                cmap=cmap,
            )
        else:
            img = ax.imshow(
                (stat.T),
                extent=[binsx[0], binsx[-1], binsy[0], binsy[-1]],
                
                origin="lower",
                norm=LogNorm(vmin=vmin, vmax=vmax),
                cmap=cmap,
            )
    else:
        if xlog and ylog:
            img = ax.imshow(
                (stat.T),
                extent=np.log10([binsx[0], binsx[-1], binsy[0], binsy[-1]]),
                
                origin="lower",
                vmin=vmin,
                vmax=vmax,
                cmap=cmap,
            )
        elif xlog:
            img = ax.imshow(
                (stat.T),
                extent=[np.log10(binsx[0]), np.log10(binsx[-1]), binsy[0], binsy[-1]],
                
                origin="lower",
                vmin=vmin,
                vmax=vmax,
                cmap=cmap,
            )
        elif ylog:
            img = ax.imshow(
                (stat.T),
                extent=[binsx[0], binsx[-1], np.log10(binsy[0]), np.log10(binsy[-1])],
                
                origin="lower",
                vmin=vmin,
                vmax=vmax,
                cmap=cmap,
            )
        else:
            img = ax.imshow(
                (stat.T),
                extent=[binsx[0], binsx[-1], binsy[0], binsy[-1]],
                
                origin="lower",
                vmin=vmin,
                vmax=vmax,
                cmap=cmap,
            )


    ax.grid()

    if cb:
        plt.colorbar(img, cax=cax)
        # cax.set_yscale('log')
        cax.set_ylabel(cax_label)
        cax.yaxis.set_label_position("right")
        cax.yaxis.set_tick_params(
            left=False, labelleft=False, right=True, labelright=True, which="both"
        )
        # cax.yaxis.set_tick_params(left=False,labelleft=False,right=False,labelright=False,which='minor')

        # cax_ticks=cax.get_yticklabels()
        # cax.set_yticklabels(["%.1e"%10**float(tick.get_text()) for tick in cax_ticks])

        return (hist_x_ax, hist_y_ax, cax)
    
    else:

        return (hist_x_ax, hist_y_ax)
