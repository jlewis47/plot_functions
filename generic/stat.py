from scipy.stats import binned_statistic
import numpy as np

def mass_function(xs, xbins, scale='log'):
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