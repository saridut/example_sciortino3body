#!/usr/bin/env python

import numpy as np

#-------------------------------------------------------------------------------

def write_xyz(config, fn, title=''):
    '''
    Writes configuration to an XYZ file.  

    '''

    na = len(config.atoms)

    with open(fn,'w') as fh:
        fh.write(str(na) + '\n')
        fh.write(title + '\n')

        for i in range(1, na+1):
            coords = config.atoms[i]['coords']
            fh.write('  '.join(['% 15.6f'%x for x in coords]) + '\n')

#-------------------------------------------------------------------------------

def write_ldf(config, fn, title=''):
    '''
    Writes configuration to a LAMMPS data file (can be imported in Ovito).

    '''

    with open(fn,'w') as fh:
        fh.write('#' + title + '\n')

        fh.write('%d atoms\n'%(len(config.atoms)))
        fh.write('%d atom types\n'%(len(config.atom_types)))

        if len(config.bonds) > 0:
            fh.write('%d bonds\n'%(len(config.bonds)))
            fh.write('%d bond types\n'%(len(config.bond_types)))

        if len(config.angles) > 0:
            fh.write('%d angles\n'%(len(config.angles)))
            fh.write('%d angle types\n'%(len(config.angle_types)))

        if len(config.dihedrals) > 0:
            fh.write('%d dihedrals\n'%(len(config.dihedrals)))
            fh.write('%d dihedral types\n'%(len(config.dihedral_types)))

        fh.write('0.0  %.8g  xlo xhi\n'%(config.simbox[0]))
        fh.write('0.0  %.8g  ylo yhi\n'%(config.simbox[1]))
        fh.write('0.0  %.8g  zlo zhi\n'%(config.simbox[2]))
        fh.write('0  0  0  xy xz yz\n') #Tilt factors

        fh.write('\n')
        fh.write('Masses\n')
        fh.write('\n')

        for iat in range(1, len(config.atom_types)+1):
            mass = config.atom_types[iat]['mass']
            buf = '%d  %.8g  '%(iat, mass) + '\n'
            fh.write(buf)

        fh.write('\n')
        fh.write('Atoms # full\n')
        fh.write('\n')

        for iatm in range(1, len(config.atoms)+1):
            imol = config.atoms[iatm]['mol_id'] 
            at = config.atoms[iatm]['type']
            chge = config.atoms[iatm]['charge']
            coords = config.atoms[iatm]['coords']
            buf = '%d  %d  %d  %.8g  '%(iatm, imol, at, chge) \
                + '  '.join( ['% .8g'%x for x in coords] )\
                + '\n'
            fh.write(buf)

        if len(config.bonds) > 0:
            fh.write('\n')
            fh.write('Bonds\n')
            fh.write('\n')
            for i in range(1, len(config.bonds)+1):
                bt = config.bonds[i]['type']
                atm_i = config.bonds[i]['atm_i']
                atm_j = config.bonds[i]['atm_j']
                buf = '%d  %d  %d  %d\n'%(i, bt, atm_i, atm_j)
                fh.write(buf)

        if len(config.angles) > 0:
            fh.write('\n')
            fh.write('Angles\n')
            fh.write('\n')
            for i in range(1, len(config.angles)+1):
                ant   = config.angles[i]['type']
                atm_i = config.angles[i]['atm_i']
                atm_j = config.angles[i]['atm_j']
                atm_k = config.angles[i]['atm_k']
                buf = '%d  %d  %d  %d  %d\n'%(i, ant, atm_i, atm_j, atm_k)
                fh.write(buf)

        if len(config.dihedrals) > 0:
            fh.write('\n')
            fh.write('Dihedrals\n')
            fh.write('\n')
            for i in range(1, len(config.dihedrals)+1):
                dt    = config.dihedrals[i]['type']
                atm_i = config.dihedrals[i]['atm_i']
                atm_j = config.dihedrals[i]['atm_j']
                atm_k = config.dihedrals[i]['atm_k']
                atm_l = config.dihedrals[i]['atm_l']
                buf = '%d  %d  %d  %d  %d  %d\n'%(i, dt, atm_i, atm_j, atm_k, atm_l)
                fh.write(buf)

#-------------------------------------------------------------------------------

