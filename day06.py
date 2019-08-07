# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:42:47 2019

@author: Andreas
Thanks to /u/sbjf on Reddit for heavy inspiration 
"""

import csv
import numpy as np
from collections import Counter
from scipy.spatial.distance import cdist

coords = np.array([[int(x), int(y)] for x, y in csv.reader(open("day06_input.txt"))])
ranges = np.array([np.min(coords, axis=0), np.max(coords, axis=0)])
axes = [np.arange(MIN, MAX+1) for MIN, MAX in ranges.T]
grid = np.array(np.meshgrid(axes[0], axes[1], indexing='ij')).reshape(2, -1).T

dists = cdist(grid, coords, metric="cityblock")
minDists = np.min(dists, axis=1)
d = (minDists[:, None] == dists)
unique = (np.sum(d, axis=1) == 1)
d = d[unique]

borders = np.any(ranges[:, None] == grid, axis=(0, -1))[unique]
dInf = np.any(d[borders], axis=0)
dArea = np.sum(d, axis=0)
dArea[dInf] = -1

print("Part one: {0}".format(max(dArea)))
print("Part one: {0}".format(np.sum(np.sum(dists, axis=1) < 10000)))