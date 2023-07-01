#convenience functions for creating labels

unit_dict = {
    "cm":"cm",
    "m":"m",
    "km":"km",
    "s":"s",
    "pc":"pc",
    "kpc":"kpc",
    "mpc":"Mpc",
    "gpc":"Gpc",
    "yr":"yr",
    "myr":"Myr",
    "gyr":"Gyr",
    "msun":"M_\odot",
    "kg":"kg",
    "g":"g",
}

#labels generated from strings
#strings contain c(comoving)+-+unit+exponent
def unit_to_label(unit, log=False):
    
    units = unit.split(".")
    label_elems=[]

    label=r""
    
    

    for u in units:

        prefix = ""
        if u.split("-")[0] == "c" or u.split("-")[0] == "p":

            prefix = u.split("-")[0]

            label += prefix

            lu = u.split("-")[1].split("^")[0]

        else:

            lu = u.split("-")[0].split("^")[0]

        exp=""
        if "^" in u:
            exp = u.split("^")[-1]

        if lu in unit_dict.keys():
            lu = unit_dict[lu]

        # print("prefix",prefix,
        #       "unit",lu,
        #       "exponent",exp)

        if exp == "":
            label_elems.append(f"{prefix:s}{lu:s}")
        else:
            label_elems.append(f"{prefix:s}{lu:s}^"+"{"+f"{exp:s}"+"}")

    final_label = r"$\mathrm{"+".".join(label_elems)+r"}$"
    if log:
        final_label = r"$\mathrm{log_{10}("+final_label+")}$"

    return(final_label)
           
def make_label(name, unit, log=False):
    label = r"$\mathrm{"+name+"}$"
    if unit != "":
        label += r", "+unit_to_label(unit,log=log)
    return(label)

# test_units=["c-cm^-3","mag^-1.c-mpc^-3.h^3","msun.myr^-1"]

# for u in test_units:
#     print(u)
#     print(unit_to_label(u,log=False))