def read_spec_names(codefile='./metadata/gckpp_Parameters.f90'):
    
    pattern = 'INTEGER, PARAMETER :: ind_'
                
    with open (codefile, "r") as f:
        spec_names = [line.replace(pattern,'').split()[0] for line in f if pattern in line]

    return spec_names

def get_redundant_specs():
    dummy_spec = ['LBRO2H', 'LBRO2N', 'LISOPOH', 'LISOPNO3', 'LTRO2H', 'LTRO2N', 'LXRO2H', 'LXRO2N']

    # CO2 is force to be zero in C_before
    # H20 is already defined in PHY
    # H2/N2/O2 are determined by NUMDEN
    fixed_spec = ['CO2', 'H2O', 'H2', 'MOH', 'N2', 'O2', 'RCOOH']

    family_spec = ['POx', 'LOx', 'PCO', 'LCO', 'PSO4', 'LCH4', 'PH2O2']
    
    return dummy_spec + fixed_spec + family_spec

def read_jval_names(codefile='./metadata/FJX_j2j.dat', njvals=130):

    varnames = [None]*njvals

    with open (codefile, "r") as f:
        line = f.readline() # skip the first line
        while line:
            linesplit = f.readline().replace('/', ' ').split()
            j = int(linesplit[0]) 
            name = ''.join([str(j), '/', linesplit[1], '/', linesplit[-1]])
            varnames[j-1] = name # use 0-based indexing
            
            if j == njvals:
                break        
    
    return varnames

def get_used_jvals(codefile='./metadata/Standard.eqn'):
    import re
    pattern = 'PHOTOL('
    indices = []

    with open (codefile, "r") as f:
        for line in f:
            if pattern in line:
                match = re.search('PHOTOL\(.*?\)', line)
                idx = int(match.group(0)[7:-1]) - 1 # 0-based indexing
                indices.append(idx)

    return indices

def get_phy_names():
    return ['TEMP', 'PRESS', 'NUMDEN', 'H2O']