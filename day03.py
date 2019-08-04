# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 19:05:42 2018

@author: Andreas
"""

import re
import numpy as np
claims = []
with open("day03_input.txt") as file:
    for claim in file:
        claims.append([int(i) for i in re.findall(r"-?\d+", claim)])


# PART ONE
def fabricHeatmap(claims):
    fabric = np.zeros([1000, 1000])
    for claim in claims:
        fabric[claim[2]:claim[2]+claim[4],
               claim[1]:claim[1]+claim[3]] += 1
    return fabric


def cellsAbove(fabric, n):
    above = 0
    for cell in fabric.flatten():
        if cell > 1:
            above += 1
    return above


# PART TWO
def getUniqueClaim(claims):
    endFabric = fabricHeatmap(claims)
    for claim in claims:
        subset = endFabric[claim[2]:claim[2]+claim[4],
                           claim[1]:claim[1]+claim[3]]
        checksum = np.sum((subset - 1).flatten())
        if checksum == 0:
            return claim[0]


# Priting results
print("Answer to part one is: %d"
      % (cellsAbove(fabricHeatmap(claims), 1)))
print("Answer to part two is: #%d"
      % (getUniqueClaim(claims)))