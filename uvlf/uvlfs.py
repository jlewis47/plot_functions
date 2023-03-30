import numpy as np
import matplotlib.pyplot as plt
from halo_properties.params.params import *
from ..generic.stat import mass_function
from ..generic.plot_functions import mf_plot
from .LF_constraints_mix import *

import os

def make_uvlf(mags, bins, box_size):
    """make uvlf from stellar masses and bins

    Args:
        mags (_type_): magnitudes in same units as bins
        bins (_type_): bins for uvlf
        box_size (_type_): size of box in cMpc
    """

    bins, uvlf_no_units = mass_function(mags, bins, scale='linear')

    return(bins, uvlf_no_units / box_size**3)

def uvlf_plot(fig, ax, mag_bins, uvlfs, redshift):



    # plot_args = {'ls':'-', 'lw':3}

    lines = mf_plot(fig, ax, mag_bins, uvlfs,
    xlabel='$\mathrm{M_{AB1600}}$', ylabel="$\mathrm{UVLF, M_\odot^{-1}.cMpc^{-3}}$",
    xscale='linear', yscale='log')        

    if not os.path.isdir('./figs/'): os.makedirs('./figs/')

    ax.set_title(f'z={redshift:.1f}')

    ax.invert_xaxis()

    return(lines)

    # fig.savefig(f'./figs/uvlf_comparison_{out_nb:d}')


def plot_constraints(fig, ax, tgt_zed, prec_zed=0.5, color='k'):

    uvlf_constr_dict=get_LF_constr()

#print(uvlf_constr_dict.keys())

    bouwens15_uvlfs=uvlf_constr_dict['bouwens15']
    bouwens17_uvlfs=uvlf_constr_dict['bouwens17']
    bouwens21_uvlfs=uvlf_constr_dict['bouwens21']
    oesch18_uvlfs=uvlf_constr_dict['oesch18']
    ono18_uvlfs=uvlf_constr_dict['ono18']
    ishigaki18_uvlfs=uvlf_constr_dict['ishigaki18']
    atek18_uvlfs=uvlf_constr_dict['atek18']
    livermore17_uvlfs=uvlf_constr_dict['livermore17']
    bowler20_uvlfs=uvlf_constr_dict['bowler20']

    coda25=np.array([  1.51978600e-04,   0.00000000e+00,   1.51978600e-04,
            3.03957200e-04,   4.55935801e-04,   7.59893001e-04,
            1.36780740e-03,   1.82374320e-03,   3.95144360e-03,
            5.01529381e-03,   8.66278021e-03,   1.21582880e-02,
            1.56537958e-02,   2.27967900e-02,   3.13075916e-02,
            4.40737941e-02,   5.31925101e-02,   6.85423487e-02,
            8.17644869e-02,   1.03497427e-01,   1.23558602e-01,
            1.62617102e-01,   1.99395923e-01,   2.33287151e-01,
            3.35112813e-01,   3.16723403e-01,   3.00005757e-01,
            3.40736022e-01,   4.24476230e-01,   5.64296542e-01,
            7.25545837e-01,   8.98497484e-01,   1.07813619e+00,
            1.09774143e+00,   1.15746902e+00,   7.29953217e-01,
            2.55628006e-01,   6.07914401e-04,   0.00000000e+00,
            0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
            0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
            0.00000000e+00,   4.49727475e+01,   0.00000000e+00,
            0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
            0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
            0.00000000e+00])

    coda25_ext=np.array([  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
            1.51978600e-04,   0.00000000e+00,   1.51978600e-04,
            9.11871601e-04,   1.82374320e-03,   3.34352920e-03,
            5.77518681e-03,   9.11871601e-03,   1.15503736e-02,
            1.59577530e-02,   2.26448114e-02,   3.23714418e-02,
            4.46817085e-02,   5.28885529e-02,   6.86943273e-02,
            8.19164655e-02,   1.03649405e-01,   1.23558602e-01,
            1.62617102e-01,   1.99395923e-01,   2.33287151e-01,
            3.35112813e-01,   3.16723403e-01,   3.00005757e-01,
            3.40736022e-01,   4.24476230e-01,   5.64296542e-01,
            7.25545837e-01,   8.98497484e-01,   1.07813619e+00,
            1.09774143e+00,   1.15746902e+00,   7.29953217e-01,
            2.55628006e-01,   6.07914401e-04,   0.00000000e+00,
            0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
            0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
            0.00000000e+00,   4.49727475e+01,   0.00000000e+00,
            0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
            0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
            0.00000000e+00])

    coda25_bins=np.array([-23. , -22.5, -22. , -21.5, -21. , -20.5, -20. , -19.5, -19. ,
        -18.5, -18. , -17.5, -17. , -16.5, -16. , -15.5, -15. , -14.5,
        -14. , -13.5, -13. , -12.5, -12. , -11.5, -11. , -10.5, -10. ,
            -9.5,  -9. ,  -8.5,  -8. ,  -7.5,  -7. ,  -6.5,  -6. ,  -5.5,
            -5. ,  -4.5,  -4. ,  -3.5,  -3. ,  -2.5,  -2. ,  -1.5,  -1. ,
            -0.5,   0. ,   0.5,   1. ,   1.5,   2. ,   2.5,   3. ,   3.5,
            4. ,   4.5])

    codaii_bins=np.array([-23.5, -23. , -22.5,
        -22. , -21.5, -21. , -20.5, -20. , -19.5, -19. , -18.5, -18. ,
        -17.5, -17. , -16.5, -16. , -15.5, -15. , -14.5, -14. , -13.5,
        -13. , -12.5, -12. , -11.5, -11. , -10.5, -10. ,  -9.5,  -9. ,
            -8.5,  -8. ,  -7.5,  -7. ,  -6.5,  -6. ,  -5.5,  -5. ,  -4.5,
            -4. ,  -3.5,  -3. ])

    codaii_z6=np.array([-5.57999992, -5.57999992, -4.80000019, -4.40999985,
        -4.17000008, -3.79999995, -3.47000003, -3.21000004, -3.        ,
        -2.70000005, -2.5       , -2.32999992, -2.1500001 , -1.98000002,
        -1.83000004, -1.67999995, -1.52999997, -1.40999997, -1.29999995,
        -1.17999995, -1.08000004, -0.98000002, -0.88999999, -0.81999999,
        -0.77999997, -0.75999999, -0.85000002, -0.93000001, -0.92000002,
        -0.95999998, -0.94      , -0.93000001, -0.95999998, -1.02999997,
        -1.12      , -1.12      , -1.49000001, -3.07999992,         0.0,
                0.0,         0.0,         0.0])



    lines=[]
    labels=[]


    #contraints
    oesch18_zeds=oesch18_uvlfs[0]
    if np.any(np.isclose(oesch18_zeds,tgt_zed, atol=prec_zed)):

            #only 1 redshift here no need for extra args
    
            oesch=ax.errorbar(oesch18_uvlfs[1][0][:,0]-.1,(oesch18_uvlfs[1][0][:,1]*1e-4),
                        yerr=([(oesch18_uvlfs[1][0][:,1]-oesch18_uvlfs[1][0][:,2])*1e-4,
                                (oesch18_uvlfs[1][0][:,1]+oesch18_uvlfs[1][0][:,3])*1e-4]),
                        linestyle='none',elinewidth=2.,
                        drawstyle='steps-mid',zorder=10.,linewidth=2,color=color,
                        fmt='^',mec=color,mfc='none',mew=1.5,capsize=3,
                        uplims=oesch18_uvlfs[1][1])     


            
            if not any(['Oesch+18' in obs_label for obs_label in labels]):
                    labels.append('Oesch+18')
                    lines.append(oesch)


                    
    atek18_zeds=atek18_uvlfs[0]
    if np.any(np.isclose(atek18_zeds,tgt_zed, atol=prec_zed)):

            #only 1 redshift here no need for extra args
    
            atek=ax.errorbar(atek18_uvlfs[1][0][:,0]+.1,10**(atek18_uvlfs[1][0][:,1]),
                        yerr=[np.abs(10**atek18_uvlfs[1][0][:,1]-10**(atek18_uvlfs[1][0][:,1]-atek18_uvlfs[1][0][:,2])),
                        np.abs(-10**atek18_uvlfs[1][0][:,1]+10**(atek18_uvlfs[1][0][:,1]+atek18_uvlfs[1][0][:,2])),      ],
                        linestyle='none',elinewidth=2.,
                        drawstyle='steps-mid',zorder=10.,linewidth=2,color=color,
                        fmt='D',mec=color,mfc='none',mew=1.5,capsize=3)

            if not any(['Atek+18' in obs_label for obs_label in labels]):
                    labels.append('Atek+18')
                    lines.append(atek)

            

    bouwens17_zeds=bouwens17_uvlfs[0]
    if np.any(np.isclose(bouwens17_zeds,tgt_zed, atol=prec_zed)):

            #only 1 redshift here no need for extra args
    
            bouwens17=ax.errorbar(bouwens17_uvlfs[1][0][0],(bouwens17_uvlfs[1][0][1]),
                        yerr=([-bouwens17_uvlfs[1][0][2],
                                bouwens17_uvlfs[1][0][3]]),
                        linestyle='none',elinewidth=2.,
                        drawstyle='steps-mid',zorder=10.,linewidth=2,color=color,
                        fmt='H',mec=color,mfc='none',mew=1.5,capsize=3)     

            if not any(['Bouwens+17' in obs_label for obs_label in labels]):                        
                    labels.append('Bouwens+17')
                    lines.append(bouwens17)


            
    ono18_zeds=ono18_uvlfs[0]
    if np.any(np.isclose(ono18_zeds, tgt_zed, atol=prec_zed)):

            ono_z_arg=np.argmin(np.abs(ono18_zeds-tgt_zed))

            ono_err_switch=np.int8(ono18_uvlfs[1][ono_z_arg][3]!=0)
            
            ono=ax.errorbar(ono18_uvlfs[1][ono_z_arg][0],10**(ono18_uvlfs[1][ono_z_arg][1]),
                        yerr=([(10**ono18_uvlfs[1][ono_z_arg][1]-10**ono18_uvlfs[1][ono_z_arg][2])*ono_err_switch,
                                (10**ono18_uvlfs[1][ono_z_arg][3]-10**ono18_uvlfs[1][ono_z_arg][1])*ono_err_switch]),
                        linestyle='none',elinewidth=2.,
                        drawstyle='steps-mid',zorder=10.,linewidth=2,color=color,
                        fmt='X',mec=color,mfc='none',mew=1.5,capsize=3)     

            if not any(['Ono+18' in obs_label for obs_label in labels]):                        
                    labels.append('Ono+18')
                    lines.append(ono)

            
            
    bouwens21_zeds=bouwens21_uvlfs[0]
    if np.any(np.isclose(bouwens21_zeds, tgt_zed, atol=prec_zed)):

            #only 1 redshift here no need for extra args
            bouwens_z_arg=np.argmin(np.abs(bouwens21_zeds-tgt_zed))
    
            bouwens21=ax.errorbar(bouwens21_uvlfs[1][bouwens_z_arg][0],(bouwens21_uvlfs[1][bouwens_z_arg][1]),
                        yerr=bouwens21_uvlfs[1][bouwens_z_arg][2],
                        linestyle='none',elinewidth=2.,
                        drawstyle='steps-mid',zorder=10.,linewidth=2,color=color,
                        fmt='o',mec=color,mfc='none',mew=1.5,capsize=3,
                        label='Bouwens+21',uplims=bouwens21_uvlfs[1][bouwens_z_arg][3]==1)

            if not any(['Bouwens+21' in obs_label for obs_label in labels]):                        
                    labels.append('Bouwens+21')
                    lines.append(bouwens21)

            


    ishigaki18_zeds=ishigaki18_uvlfs[0]
    if np.any(np.isclose(ishigaki18_zeds,tgt_zed, atol=prec_zed)):
            
            ishigaki_z_arg=np.argmin(np.abs(ishigaki18_zeds-tgt_zed))
            
            ishigaki=ax.errorbar(ishigaki18_uvlfs[1][ishigaki_z_arg][0][0,:],10**(ishigaki18_uvlfs[1][ishigaki_z_arg][0][1,:]),
                        yerr=([np.abs(10**ishigaki18_uvlfs[1][ishigaki_z_arg][0][1,:]-10**ishigaki18_uvlfs[1][ishigaki_z_arg][1][1,:]),
                                np.abs(10**ishigaki18_uvlfs[1][ishigaki_z_arg][0][1,:]-10**ishigaki18_uvlfs[1][ishigaki_z_arg][2][1,:])]),
                        linestyle='none',elinewidth=2.,
                        drawstyle='steps-mid',zorder=10.,linewidth=2,color=color,
                        fmt='s',mec=color,mfc='none',mew=1.5,capsize=3,
                                    uplims=ishigaki18_uvlfs[1][ishigaki_z_arg][-1])


            if not any(['Ishigaki+18' in obs_label for obs_label in labels]):                        
                    labels.append('Ishigaki+18')
                    lines.append(ishigaki)


    bowler20_zeds=bowler20_uvlfs[0]
    if np.any(np.isclose(bowler20_zeds,tgt_zed, atol=prec_zed)):
            
            bowler_z_arg=np.argmin(np.abs(bowler20_zeds-tgt_zed))
            
            bowler=ax.errorbar(bowler20_uvlfs[1][bowler_z_arg][:,0],1e-6*(bowler20_uvlfs[1][bowler_z_arg][:,1]),
                        yerr=1e-6*np.abs(bowler20_uvlfs[1][bowler_z_arg][:,1]-bowler20_uvlfs[1][bowler_z_arg][:,2]),
                        linestyle='none',elinewidth=2.,
                        drawstyle='steps-mid',zorder=10.,linewidth=2,color=color,
                        fmt='P',mec=color,mfc='none',mew=1.5,capsize=3)
            

            if not any(['Bowler+20' in obs_label for obs_label in labels]):                        
                    labels.append('Bowler+20')
                    lines.append(bowler)

    return(lines, labels)