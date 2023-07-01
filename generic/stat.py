from scipy.stats import binned_statistic, binned_statistic_2d
from scipy.spatial import cKDTree
import numpy as np

def mass_function(xs=[], xbins=[], scale='log'):
    """generic wrapper for making a mass function

    Args:
        xs (_type_): xdata same units as xbins
        ys (_type_): ydata
        scale (_type_): either log or linear

        xs and ys must have the same dimension
        xbins (_type_): bins
    """

    assert scale=='log' or scale=='linear', "didn't understand required scale"

    rslt, bins, cnts = binned_statistic(xs, xs, 'count', bins=xbins)
    pois_err = np.sqrt(rslt)

    if scale=='log':
        return(bins[:-1] + 0.5*np.diff(xbins), rslt/np.diff(np.log10(xbins)), pois_err/np.diff(np.log10(xbins)))
    if scale=='linear':
        return(bins[:-1] + 0.5*np.diff(xbins), rslt/np.diff(xbins), pois_err/np.diff(xbins))

def cosmic_variance(function, properties, coordinates, volume, sub_volume, nsub):

    sub_r = np.cbrt(sub_volume)/4.*3./np.pi
    ldx = np.cbrt(volume)

    coords_tree = cKDTree(coordinates, boxsize = ldx+1e-6)

    results=[]

    for isub in range(nsub):

        loc_coord = np.random.uniform(low=0, high=ldx, size=3)

        loc_prop = properties[coords_tree.query_ball_point(loc_coord, r=sub_r)]
        results.append(function(loc_prop))

    return(results)

def xy_stat(xs, ys, xbins, mthd='mean'):
    """generic wrapper for binned_statistic

    Args:
        xs (_type_): xdata same units as xbins
        ys (_type_): ydata

        xs and ys must have the same dimensfiles.
        xbins (_type_): bins
        mthd (see binned_statistic methods)
    """

    rslt, bins, cnts = binned_statistic(xs, ys, mthd, bins=xbins)

    return(bins[:-1] + 0.5*np.diff(xbins), rslt)   


def xy_2Dstat(xs, ys, xbins, ybins, mthd='count'):
    """generic wrapper for binned_statistic2D

    Args:
        xs (_type_): xdata same units as xbins
        ys (_type_): ydata

        xs and ys must have the same dimensfiles.
        xbins (_type_): bins
        ybins (_type_): bins
        mthd (see binned_statistic methods)
    """

    rslt, xbins, ybins, cnts = binned_statistic_2d(xs, ys, ys, mthd, bins=[xbins, ybins])

    return(xbins[:-1] + 0.5*np.diff(xbins), ybins[:-1] + 0.5*np.diff(ybins),  rslt)             