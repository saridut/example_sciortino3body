#!/usr/bin/env bash

LAMMPS_BIN="path to LAMMPS binary"

FN_INP='inp_AB.txt' #Input file name
FN_LOG='log.txt'    #LAMMPS file name

TRAJ_DIR='traj'      #Location of LAMMPS dump files
RESTART_DIR='revive' #Location of LAMMPS restart files

if [ -d ${TRAJ_DIR} ]; then
    rm -rf ${TRAJ_DIR}/*
else
    mkdir ${TRAJ_DIR}
fi

if [ -d ${TRAJ_DIR} ]; then
    rm -rf ${RESTART_DIR}/*
else
    mkdir ${RESTART_DIR}
fi

${LAMMPS_BIN} -l ${FN_LOG} -in ${FN_INP}
