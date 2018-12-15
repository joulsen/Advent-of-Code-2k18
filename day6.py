# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 22:30:11 2018

@author: Andreas
"""

import numpy as np
from collections import Counter
data = np.loadtxt("day6_input.txt", delimiter=", ", dtype=int)


# PART ONE
def taxaDist(coord1, coord2):
    return abs(coord2[0] - coord1[0]) + abs(coord2[1] - coord1[1])


def getClosest(ref, coordList):
    cI = cLen = 10000000
    for i in range(len(coordList)):
        if taxaDist(ref, coordList[i]) < cLen:
            cI = i
            cLen = taxaDist(ref, coordList[i])
    return cI

x_min, y_min = data.min(0)
x_max, y_max = data.max(0) - [x_min, y_min]
data = np.array([row-[x_min,y_min]+[5,5] for row in data])
grid = np.zeros(shape=[y_max+10, x_max+10], dtype=int)
for y in range(y_max+5):
    for x in range(x_max+5):
        grid[y,x] = getClosest([y,x], data)
counter = Counter(grid.flatten())
edges = np.concatenate((grid[:,0], grid[:,x_max], grid[0,:], grid[y_max,:]))
for element in edges:
    try:
        counter.pop(element)
    except KeyError:
        pass