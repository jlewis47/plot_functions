import numpy as np
import matplotlib.pyplot as plt
import os
# from generic.stat import xy_stat
from ..generic.plot_functions import xy_plot, density_plot_fancy
from ..utils.utils import get_mod_path
import h5py
import csv



def lesc_plot(fig, ax, masses, lescs, lesc_type, xlabel, redshift=None, log=True, **plot_args):


    lesc_labels = {'gas':"$\mathrm{L_{esc, g}}$",
                'dust':"$\mathrm{L_{esc, d}}$",
                'full':"$\mathrm{L_{esc, gxd}}$"}

    if log:
        lines = xy_plot(fig, ax, masses, lescs,
        xlabel=xlabel, ylabel=lesc_labels[lesc_type],
        xscale='log', yscale='log', **plot_args)        
    else:
        lines = xy_plot(fig, ax, masses, lescs,
        xlabel=xlabel, ylabel=lesc_labels[lesc_type],
        **plot_args)        
    # if not os.path.isdir('./figs'): os.makedirs('./figs')

    if redshift!=None:
        ax.set_title(f'z={redshift:.1f}')

    # fig.savefig(f'./figs/lesc_comparison_{lesc_type:s}_{out_nb:d}')
    return(lines)




def lesc_Mh_plot(fig, ax, masses, lescs, lesc_type, redshift=None, log=True, **plot_args):


    return(lesc_plot(fig, ax, masses, lescs, lesc_type, '$\mathrm{Halo \, \, masses, \, M_\odot}$', redshift, log=log, **plot_args))

def lesc_Mst_plot(fig, ax, masses, lescs, lesc_type, redshift=None, log=True, **plot_args):

    return(lesc_plot(fig, ax, masses, lescs, lesc_type, '$\mathrm{Stellar \, \, masses, \, M_\odot}$', redshift, log=log, **plot_args))


def plot_ndot(fig, ax, redshifts, lescs, **plot_args):

    lines=xy_plot(fig, ax, redshifts, lescs, xlabel='redshift', ylabel='$\mathrm{\dot{N_{ion}}, \, s^{-1}.cMpc^{-3}.h^3}$', xscale='linear', yscale='log', **plot_args)

    ax.invert_xaxis()

    return(lines)

def plot_lesc_density(fig, ax, nbs, binsx, binsy, lesc_type, cb=True, **kwargs):

    lesc_labels = {'gas':"$\mathrm{L_{esc, g}}$",
                'dust':"$\mathrm{L_{esc, d}}$",
                'full':"$\mathrm{L_{esc, gxd}}$"}


    density_plot_fancy(fig, ax, nbs, nbs, binsx, binsy, xlabel="$\mathrm{Halo \, \, masses, \, M_\odot}$", ylabel=lesc_labels[lesc_type], cb=cb, **kwargs)


def plot_dustier_lesc(ax, redshift, fkey="lesc", zprec=0.1, **plot_args):

    dir_path = get_mod_path()

    assert (fkey=="lesc" or fkey=="lesc_total"), "fkey must be either lesc or lesc_total"

    with h5py.File(os.path.join(dir_path,"../constraints/dustier_median_lescs")) as src:

        redshifts = src['redshifts'][()]
        masses = src['mbins'][()]
        lescs = src[fkey][()]

    dist = np.abs(redshift - redshifts)

    if np.any(dist):

        whs = np.argmin(dist)

        l,=ax.plot(masses, lescs[whs], **plot_args)

    label="DUSTiER"

    return([l],[label])

def plot_cosmic_ndot_constraints(ax, redshift, zprec=0.5, **plot_args):

    dir_path = get_mod_path()

    
    with h5py.File(os.path.join(dir_path,"../constraints/cosmic_ndot_constraints.hdf5"), 'r') as src:
            
        puchwein19 = src['puchwein19'][()]
        bouwens15a = src['bouwens15a'][()]
        kulkarni_19_nphot = src['kulkarni_19_nphot'][()]
        keating_19_nphot = src['keating_19_nphot'][()]
        fink_ndot_2019 = src['fink_ndot_2019'][()]
        zbb13, lgambb13, erplgbb13, ermlgbb13 = src['bolton_ndot_13'][()]

    b13=ax.errorbar(zbb13,10**(lgambb13+51),yerr=[10**(erplgbb13+51)-1e51,-1e51+10**(-ermlgbb13+51)],fmt='^',color='b',mec='b',label=r"Becker-Bolton13")
    bw15=ax.scatter(bouwens15a[:,0],10**bouwens15a[:,1],linewidth=3,marker='p',color='navy',label='Bouwens+15a from UVLF',s=65)     
    ma17=ax.fill_between([5,6],[2e50,3e50],[5e50,5e50],alpha=0.3,color='cyan',label='Madau+17')
    f19,=ax.plot(fink_ndot_2019[0],10**fink_ndot_2019[1],label='Finkelstein+19',linewidth=3,linestyle='--')
    ke19,=ax.plot(keating_19_nphot[0],keating_19_nphot[1]*1e50,label='Keating+19',linewidth=3,linestyle='--')
    ku19,=ax.plot(kulkarni_19_nphot[0],kulkarni_19_nphot[1]*1e50,label='Kulkarni+19',linewidth=3,linestyle='--')
    p19,=ax.plot(puchwein19[:,0],10**puchwein19[:,1],linewidth=3,linestyle='-.',color='k',label='Puchwein+19 fiducial galaxies')                                                                     






    

    return([b13, bw15, ma17, f19, ke19, ku19, p19], ["Becker-Bolton+13", "Bouwens+15a", "Madau+17", "Finkelstein+19", "Keating+19", "Kulkarni+19", "Puchwein+19 (galaxies)"])

def plot_Mh_lesc_constraints(ax, redshift, zprec=0.5, log=False, **plot_args):

    if log==True:
        scale_fct = lambda x: np.log10(x)
    else:
        scale_fct = lambda x: x


    dir_path = get_mod_path()

    labels=[]
    lines=[]

   
    return(lines, labels)