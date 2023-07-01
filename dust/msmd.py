import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
import h5py
from ..utils.utils import get_mod_path
from ..generic.plot_functions import xy_plot

def plot_msmd(fig, ax, ms, md, redshift=None, **plot_args):


    line = xy_plot(fig, ax, ms, md, xlabel="$\mathrm{Stellar \, Mass, \, M_\odot}$", ylabel="$\mathrm{Dust \, Mass, \, M_\odot}$",
        xscale='log', yscale='log',
        **plot_args)

    return(line)

def plot_dustier_msmd(ax, redshift, zprec=0.1, **plot_args):

    dir_path = get_mod_path()

    label="DUSTiER"

    with h5py.File(os.path.join(dir_path,"../constraints/dustier_mdms")) as src:

        keys = list(src.keys())
        redshifts = [float(k.split('_')[-1].lstrip('z')) for k in keys if "mdust" in k]
        mdust_keys = [k for k in keys if "mdust" in k]
        
        dist = np.abs(redshift - redshifts)

        # print(keys, redshifts, mdust_keys, dist)
        if np.any(dist):

            whs = np.argmin(dist)

            mstel = src['mstel'][()]/0.8
            mdusts = src[mdust_keys[whs]][()]



            l,=ax.plot(mstel, mdusts, **plot_args)

            return([l],[label])

        else:

            return([],[""])


def plot_msmd_constraints(ax, redshift, zprec=0.1):


    dir_path = get_mod_path()

    burgarella=pd.read_html(os.path.join(dir_path,'../constraints/burgarella_2020_tab'))[0]


    burg_2020_arr=burgarella.to_numpy()

    # print(burgarella)

    for ir,row in enumerate(burg_2020_arr):

        for ic,col in enumerate(row):
                    #print(col.replace(u'\u2005\xd7\u200510','e'))
                    # try:
                    if isinstance(col, str):
                        burg_2020_arr[ir,ic]=col.replace(u'\u2005\xd7\u200510','e').replace(u' \xd7 10','e')

                        try:
                            burg_2020_arr[ir,ic] = np.float32(burg_2020_arr[ir,ic])
                        except ValueError:
                            pass
                    
    burg_2020_mdust=burg_2020_arr[:,6]
    burg_2020_mdust_err=burg_2020_arr[:,7]

    burg_2020_mstar=burg_2020_arr[:,8]
    burg_2020_mstar_err=burg_2020_arr[:,9]

    popping_17_SMDM_fid=np.asarray([7.02855459411991,4.1397212413255176,
7.186658064370058,4.255883154278875,
7.344733144370272,4.395892877176298,
7.502788076451178,4.552826852292092,
7.66081919735472,4.729762216393231,
7.8224656595905095,4.890789882386519,
7.976891513121458,5.075170818486325,
8.102971774790502,5.237681086420581,
8.231113861328748,5.413713009679394,
8.370433633993057,5.599089985644607,
8.486747731060456,5.774968728750239,
8.60882164054433,5.946171475583239,
8.730875636968074,6.134101192924721,
8.845736966115117,6.321913380736909,
8.919867177640286,6.486102133160955,
9.025201099420787,6.620992452925225,
9.140074887763962,6.798338915985973,
9.26933759517793,6.972909443497677,
9.377029631033231,7.140969954415331,
9.486498949230041,7.326602808955748,
9.645910628653725,7.518694190963098,
9.81512173210034,7.703045617484119,
9.973174483670501,7.861811221627875,
10.131247256690342,8.003758808036881,
10.289339881080032,8.129031243775323,
10.447418327788839,8.266212931453571,
10.605497655423989,8.402654641004526,
10.763578103841663,8.538154893235106,
10.921655778649665,8.675984977589255,
11.079741953088565,8.806675371992407,
11.237816753983402,8.946919543405409,
11.390161891329958,9.066514661808778,
11.53066430368351,9.164768005104138,
11.633141298477433,9.181994476112122]).reshape((-1,2)).T


    popping_17_SMDM_highcond=np.asarray([7.15,4.929729220427536,
7.300000000000001,5.031834696648113,
7.450000000000001,5.171502261584088,
7.600000000000001,5.341300874887547,
7.750000000000002,5.5027970195605524,
7.900000000000002,5.648528266646936,
8.050000000000002,5.8013056693389355,
8.200000000000003,5.960528139941696,
8.350000000000003,6.130183297924011,
8.500000000000004,6.310573944399408,
8.650000000000004,6.474495780154127,
8.800000000000004,6.642925804743113,
8.950000000000005,6.818617760415403,
9.100000000000005,6.9775877718939885,
9.250000000000005,7.170126018913358,
9.400000000000006,7.342428736538492,
9.550000000000006,7.508445532541796,
9.700000000000006,7.657783671036475,
9.850000000000007,7.784173087633825,
10.000000000000007,7.946093965060314,
10.150000000000007,8.074796798064558,
10.300000000000008,8.210189469992612,
10.450000000000008,8.338970641751104,
10.600000000000009,8.450391123475768,
10.750000000000009,8.575649548636276,
10.90000000000001,8.72731849252013,
11.05000000000001,8.830291244764487,
11.20000000000001,8.945483089290093,
11.35000000000001,9.05730001792556,
11.50000000000001,9.150668920551016]).reshape((-1,2)).T


    vij_19=np.asarray([7.542056473484967,4.213420252292202,
7.618838259189522,4.280821148199196,
7.695618108160927,4.3497895068017005,
7.772397957132331,4.4187578654042055,
7.8491729642708625,4.49164488074549,
7.925944097943096,4.567666821477796,
8.002719105081628,4.6405538368190795,
8.079487333654136,4.718926971594653,
8.15625653059322,4.796516375022471,
8.233018948966281,4.8795918978845805,
8.309774588773319,4.968153540180978,
8.386527323480633,5.059066376520644,
8.463281994921097,5.148411750164798,
8.540029887795537,5.243243243243242,
8.61677778066998,5.338074736321686,
8.69351308477895,5.443094736920955,
8.770245483788196,5.550465931563491,
8.843489245375583,5.653604976928147,
9.14021283873563,5.860039813927007,
9.216909408181614,5.996409068436506,
9.2936059776276,6.132778322946004,
9.370307388906456,6.265228920716724,
9.447025262417084,6.384356085575597,
9.523744104294284,6.502699519086713,
9.607446805907912,6.624177877988853,
9.68418985694948,6.722928027806075,
9.760931939624474,6.8224619089710545,
9.83767886413234,6.918077133397254,
9.914431598839654,7.00898996973692,
9.99119304884614,7.092849223946784,
10.067956435585776,7.175141015461136,
10.144719822325412,7.257432806975489,
10.221505481496266,7.321698777491459,
10.298293077400267,7.384397285311918,
10.375075831471396,7.451014449871156,
10.451836313111308,7.535657435428776,
10.528591952918346,7.624219077725174,
10.605348561091958,7.711996988673817,
10.682162302893476,7.753534750104871,
10.758994443659912,7.780181615928566,
10.82535285260068,7.800460664551746]).reshape((-1,2)).T

    graziani_box=np.asarray([[7.5,8.4,8.6,9.5],[4,5,6,7.25]])
    graziani_up=10**graziani_box[1]+0.6*10**graziani_box[1]
    graziani_dw=10**graziani_box[1]-0.6*10**graziani_box[1]


    thesan21=np.asarray([1737317.32419, 1539.98187,
2245830.74973, 1927.54611,
2903186.24364, 2598.90932,
3752949.93458, 3578.84502,
4851439.77321, 4928.27188,
6271457.99527, 6684.97363,
8107116.07792, 8891.88822,
10480071.96261, 11667.99507,
13547592.91539, 15104.50252,
17512978.38945, 19087.18368,
22481072.91248, 23662.38639,
29265487.21837, 29396.83425,
37831506.18808, 35452.03255,
48904802.08921, 42433.45088,
63219255.81007, 50332.38719,
81723555.44736, 59972.30259,
105644070.45571, 72107.75160,
136566129.08431, 86307.62512,
176539085.74915, 98142.58889,
228212141.66441, 112275.38267,
295009920.22275, 135198.05600,
381359433.35485, 171104.15133,
492983481.02640, 213306.41657,
637279928.87687, 234644.00657,
823812000.56390, 269650.05764,
1064942078.85875, 323237.99382,
1376651020.55773, 394548.46609,
1779597285.17218, 443273.04367,
2300486070.97906, 454262.88461,
2973839197.70178, 476889.70704,
3844283034.50834, 495388.51656,
4969506105.38383, 473660.23616,
6424082386.69278, 475266.76235,
8304413685.35743, 495940.35339,
10735118652.96218, 527754.80404,
14389033788.77951, 196028.24989,
12698619132.69675, 435418.99698,
15278684180.13558, 137403.40983,
13512972015.34439, 295266.53181,
16375819064.35970, 92660.22317,
17332246327.20459, 63957.28079,
18506210155.95562, 44153.45719])
    thesan21 = thesan21.reshape((-1,2))

    labels=[]
    lines=[]

    delphi_dtg_z7=np.genfromtxt(os.path.join(dir_path,'../constraints/dayal22_dtg_z7'), delimiter=',')
    delphi_dtm_z7=np.genfromtxt(os.path.join(dir_path,'../constraints/dayal22_dtm_z7'), delimiter=',')
    delphi_dmsm_z7=np.genfromtxt(os.path.join(dir_path,'../constraints/dayal22_dmsm_z7'), delimiter=',')
    rebels_dust_masses=np.genfromtxt(os.path.join(dir_path,'../constraints/dayal22_rebels_dust'), delimiter=',',skip_header=1)


    mancini_mstar=np.asarray([9.2,9.7,9.5,9.7,9.9,9.3,9.3,9.8])      
    mancini_mdust=np.asarray([7.36,8.28,7.61,7.43,7.30,7.02,7.36,7.38])

    mancini_err_mstar_up=mancini_mstar+0.3
    mancini_err_mstar_dw=mancini_mstar-0.3
    

    if 6<=redshift<7.5:
        manc=ax.errorbar(10**mancini_mstar,10**mancini_mdust,xerr=[10**mancini_err_mstar_dw,10**mancini_err_mstar_dw],
                    yerr=-10**mancini_mdust+10**(mancini_mdust+0.2),uplims=True,
                    fmt='D',mec='navy',mfc='none',color='navy')                                                                                                
        lines.append(manc[0])
        labels.append('6<z<7.5 from Mancini+2015')

    if 5<=redshift<10:
        burg_mask=burg_2020_mdust<3e8


        burg=ax.errorbar(burg_2020_mstar[burg_mask],burg_2020_mdust[burg_mask],yerr=np.abs(burg_2020_mdust_err-burg_2020_mdust)[burg_mask],
                    xerr=np.abs(burg_2020_mstar_err-burg_2020_mstar)[burg_mask],
                    fmt='H',mec='limegreen',mfc='none',color='limegreen')
        labels.append('5<z<10 from Burgarella+2020')
        lines.append(burg[0])



    rebs=ax.errorbar(10**rebels_dust_masses[:,1], 10**rebels_dust_masses[:,7], 
                    xerr=[10**rebels_dust_masses[:,1] - 10**(-rebels_dust_masses[:,3] + rebels_dust_masses[:,1]), 
                        -10**rebels_dust_masses[:,1] + 10**(rebels_dust_masses[:,2] + rebels_dust_masses[:,1])],
                    yerr=[10**rebels_dust_masses[:,7] - 10**(-rebels_dust_masses[:,9] + rebels_dust_masses[:,7]), 
                        -10**rebels_dust_masses[:,7] + 10**(rebels_dust_masses[:,8] + rebels_dust_masses[:,7])],
                fmt='v',mec='lightskyblue',mfc='none',color='lightskyblue')
    lines.append(rebs[0])
    labels.append('Dayal+22, REBELS')

    if np.abs(redshift - 6.0)<zprec:
        popfid=ax.plot(10**popping_17_SMDM_fid[0],10**popping_17_SMDM_fid[1],linestyle='--',linewidth=2,color='magenta')
        lines.append(popfid[0])
        labels.append('Popping+17, z=6, fiducial')
            
        pophigh=ax.plot(10**popping_17_SMDM_highcond[0],10**popping_17_SMDM_highcond[1],linestyle='--',linewidth=2,color='gold')
        lines.append(pophigh[0])
        labels.append('Popping+17, z=6, high-cond')

        vij=ax.plot(10**vij_19[0],10**vij_19[1],linestyle='--',
                linewidth=2,color='cyan')
        lines.append(vij[0])
        labels.append('Vijayan+20, z=6')

    if 5.5<=redshift<6.5:
        graz=ax.fill_between(10**graziani_box[0],y1=graziani_dw,y2=graziani_up,linewidth=2,color='silver',alpha=0.4)
        lines.append(graz)
        labels.append('Graziani+20, 5.5<z<6.5')

    if np.abs(redshift - 7.0)<zprec:
        daya=ax.plot(10**delphi_dmsm_z7[:,0],10**delphi_dmsm_z7[:,1],color='brown', lw=2, ls ='--')
        lines.append(daya[0])
        labels.append('Dayal+22, z=7')

        thes=ax.plot(thesan21[:,0],thesan21[:,1],color='indigo', lw=2, ls ='--')
        lines.append(thes[0])
        labels.append('Kannan+22, z=7')


    return(lines, labels)