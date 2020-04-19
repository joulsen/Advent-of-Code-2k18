# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:48:20 2020

@author: Andreas
"""

import re
from collections import defaultdict
from itertools import product
import numpy as np

def split_line(s):
    s = map(int, re.search(r"<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)", s).groups())
    return list(s)

def nanobots_in_range(src, radius, nanobots):
    return np.sum(np.sum(np.abs(nanobots - src), axis=1) <= radius)

def part_one(total):
    strongest = max(total, key=lambda n: n[3])
    return nanobots_in_range(strongest[:3], strongest[3], nanobots)

#%% Stuff for part two - not yet finished

# Using itertools to get all 26 relative neighbor coordinates
NEIGHBORS = list(product([1,0,-1],repeat=3))
NEIGHBORS.remove((0,0,0))
NEIGHBORS = np.array(NEIGHBORS)

def get_neighbors(point):
    return point - NEIGHBORS

def in_range_nanobots(point):
    points = np.sum(np.abs(nanobots - point), axis=1)
    points.resize(len(points), 1)
    return np.sum(points <= distances)

def travel(point):
    neighbors = get_neighbors(point)
    in_range = -np.apply_along_axis(in_range_nanobots, 1, neighbors)
    from_zero = np.sum(np.abs(neighbors),1)
    total = np.array([in_range, from_zero, np.arange(0, 26)]).T
    return total

#%% Results

if __name__ == "__main__":
    with open("day23_input.txt") as file:
        total = np.array(list(map(split_line, file.readlines())))
    nanobots, distances = np.split(total, [3], 1)
    print("Answer to part 1 is: {}".format(part_one(total)))
    print("Part 2 has not (yet) been completed.")