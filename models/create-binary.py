#!/usr/bin/env python

'''
Creates initial configuration for a system containing unbonded atoms of two
types.

'''
import sys
import math
import numpy as np
from configuration import Configuration
from config_io import *

#-------------------------------------------------------------------------------

config = Configuration()

#Add simulation box and boundary condition. The box size can be updated later if
#necessary.
config.add_simbox(10.0, 10.0, 10.0, 1)

#Molecule details
# NA
#Total number of atoms in the molecule
#natm = 1

#Atom types
# atoms as point particles with mass 1.0
atm_t_A = config.add_atom_type('A', 1, 1.0)
atm_t_B = config.add_atom_type('B', 1, 1.0)
natm_A = 75
natm_B = 50

#Add atoms
sep = 1.2

#Loop over all atoms
iatm = 1 #Index of one past the last atom, bond, etc. added
for i in range(natm_A):
    iatm_beg = iatm
    config.append_atom_unbonded( atm_t_A, 0.0, sep=sep )
    iatm += 1
    
for i in range(natm_B):
    iatm_beg = iatm
    config.append_atom_unbonded( atm_t_B, 0.0, sep=sep )
    iatm += 1
    
config.apply_pbc()

write_ldf(config, 'atm_data.txt', title='test_frame')
