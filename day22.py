# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:59:33 2020

@author: Andreas
"""

DEPTH = 8103
TARGET = 9+758j

#DEPTH = 510
#TARGET = 10+10j

# Geological index
def get_GI(coord):
    if coord in GI_grid.keys(): # We must do this check or we will never compute
        return GI_grid[coord]
    elif coord == 0+0j or coord == TARGET:
        return 0
    elif coord.imag == 0:
        return coord.real * 16807
    elif coord.real == 0:
        return coord.imag * 48271
    else:
        return int(get_EL(get_GI(coord-1)) * get_EL(get_GI(coord-1j)))

# Erosion level
def get_EL(GI):
    return (GI + DEPTH) % 20183

# 0 is rocky, 1 is wet and 2 is narrow
def get_type(EL):
    return int(EL % 3)

def risk_level(grid):
    return sum(grid.values())

GI_grid = {}
type_grid = {}

for x in range(int(TARGET.real + 1)):
    for y in range(int(TARGET.imag + 1)):
        GI = get_GI(x + 1j*y)
        GI_grid[x + 1j*y] = GI
        type_grid[x + 1j*y] = get_type(get_EL(GI))