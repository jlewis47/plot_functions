import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch
import os

from ..utils.utils import get_mod_path
from ..generic.plot_functions import xy_plot
from ..generic.stat import xy_stat


def make_budget(xs, lintrs, fescs, bins):

    budget = np.zeros(len(bins)-1, dtype='f8')

    budget[:], xbins = xy_stat(xs, lintrs * fescs, bins, smthd='sum')

    return(xbins, budget)





def plot_stack_budget(fig, ax, bins, budget, redshifts, bin_labels, leg_title='', txt_size=14, cmap=None):



    zord = np.argsort(redshifts)[::-1]
    redshifts = np.asarray(redshifts)[zord]
    budget = budget[:,zord]
        
    min_z = np.min(redshifts)
    max_z = np.max(redshifts)


    normd_budget = budget
    normd_budget = normd_budget / np.sum(normd_budget, axis=0)[np.newaxis,:]

    # print(normd_budget[:,0])
    if cmap==None:
        colors = [(0.9, 0.7, 0), (0.5, 0, 0)]
        cm = LinearSegmentedColormap.from_list(
                "Custom", colors, N=len(bins)-1)
        fills=[Patch(color = cm(icolor)) for icolor in range(len(redshifts))]
        colors = [cm(imbin) for imbin in range(len(bins)-1)]

    else:
        colors = cmap(np.arange(len(redshifts))/float(len(redshifts)-2))
        fills=[Patch(color = color) for color in colors]

        

    m_budget_m1=np.zeros_like(redshifts)

    # print(normd_budget.shape)
    # print(m_budget_m1.shape)
    z_sizes = np.diff(redshifts) #integrate

    for imbin,(m_budget_p1, m_label)  in enumerate(zip(normd_budget, bin_labels)):
        
        # print(imbin)
        
        
        for ized, zed in enumerate(np.round(redshifts, decimals=1)):

            # print(ized)
            # print(m_budget_m1[ized])
            # print(m_budget_p1[ized])

            # print(zed+abs(zed-redshifts[ized-1])*0.5, zed, zed-abs(zed-redshifts[ized+1])*0.5)
            # print(cm(imbin))

            if ized == 0:
                # print([zed+1.0, zed-abs(zed-redshifts[ized+1])*0.5], m_budget_m1[ized], m_budget_m1[ized]+m_budget_p1[ized])
                ax.fill_between([zed+1.0, zed-abs(zed-redshifts[ized+1])*0.5], m_budget_m1[ized], m_budget_m1[ized]+m_budget_p1[ized], label = m_label, step='pre',color=colors[imbin]) 
            elif ized == len(redshifts)-1:
                ax.fill_between([zed+abs(zed-redshifts[ized-1])*0.5, zed-1.0], m_budget_m1[ized], m_budget_m1[ized]+m_budget_p1[ized], step='pre',color=colors[imbin])
            else:
                ax.fill_between([zed+abs(zed-redshifts[ized-1])*0.5, zed-abs(zed-redshifts[ized+1])*0.5], m_budget_m1[ized], m_budget_m1[ized]+m_budget_p1[ized], step='pre',color=colors[imbin])
                
            if 0.05<np.round(m_budget_p1[ized],decimals=2):
                ypos = m_budget_m1[ized] + m_budget_p1[ized]*0.5
                if ypos<0:
                    ypos = ypos + 0.045
                ax.text(zed, ypos, "%0.2f"%(m_budget_p1[ized]), 
                        va='center', ha='center', size=txt_size)
                
        m_budget_m1+=m_budget_p1
        
    # ax.set_title('Ionising galactic photon budget')

    ax.set_xlabel('Redshift', size=txt_size)
    ax.set_ylabel('Fraction of total escaping luminosity', size=txt_size)

    # ax.set_yscale('log')
    # ax.set_xscale('log')    
    # ax.set_ylim(1e45,2e50)
    # ax.set_xlim(1e7,1e12)

    # ax.plot(codaii_bins_budget[:-1],codaii_budget_z6,drawstyle='steps-pre',
    #                 label='CoDa II, z=6',linewidth=4,linestyle='--',color='tab:purple')
    # ax.plot(codaii_bins_budget[:-1],codaii_budget_z10,drawstyle='steps-pre',
    #                 label='CoDa II, z=10.1',linewidth=4,linestyle='--',color='tab:blue')

    ax.invert_xaxis()


    ax_divider = make_axes_locatable(ax)
    # Add an Axes to the right of the main Axes.
    lax = ax_divider.append_axes("top", size="10%", pad="5%")
    lax.axis('off')

    lax.legend(fills, bin_labels, prop={"size":txt_size},ncol=3, 
    framealpha=0.0, title=leg_title, title_fontsize=txt_size,
    loc='center', bbox_to_anchor=(0.5, 1.0))
    #ax.grid()  
    

    # ax.tick_params(which='both',direction='in',top='on',right='on')

    #fig.savefig('figs/dustier_tot_budget_NoHe.png',bbox_inches='tight')

    ax.set_ylim(0,1)

    

    ax.set_xlim(max_z+0.5,min_z-0.5)
