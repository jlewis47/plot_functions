import numpy as np
import matplotlib.pyplot as plt

def setup_plotting(scale_up=1.5):



    plt.rcParams['ytick.major.size']=15*scale_up
    plt.rcParams['ytick.major.width']=1.5*scale_up
    plt.rcParams['ytick.minor.size']=10*scale_up
    plt.rcParams['ytick.minor.width']=1*scale_up
    plt.rcParams['xtick.major.size']=15*scale_up
    plt.rcParams['xtick.major.width']=1.5*scale_up
    plt.rcParams['xtick.minor.size']=10*scale_up
    plt.rcParams['xtick.minor.width']=1*scale_up
    plt.rcParams['axes.linewidth']=1.75*scale_up
    plt.rcParams['font.size']= 16*scale_up
    #plt.rcParams['figure.dpi']= 200 
    plt.rcParams['figure.figsize']= (10,10)


def make_figure(*args,**kwargs):


    fig=plt.figure(*args,**kwargs)
    ax=fig.add_subplot(111)

    return(fig,ax)



def xy_plot(fig, ax, xs, ys, xlabel=None, ylabel=None, xscale='linear', yscale='linear'):
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

    plots = [ax.plot(x,y) for x,y in zip(xs,ys)]

    ax.grid()

    ax.set_xscale(xscale)
    ax.set_yscale(yscale)

    if xlabel != None:
        ax.set_xlabel(xlabel)
    if ylabel != None:
        ax.set_ylabel(ylabel)

    return([plot[0] for plot in plots])

def mf_plot(fig, ax, bins, mfs, xlabel=None, ylabel=None, xscale='log', yscale='log'):
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

    plots = [ax.plot(bin,mf) for bin,mf in zip(bins,mfs)]

    ax.grid()

    ax.set_xscale(xscale)
    ax.set_yscale(yscale)

    if xlabel != None:
        ax.set_xlabel(xlabel)
    if ylabel != None:
        ax.set_ylabel(ylabel)

    return([plot[0] for plot in plots])