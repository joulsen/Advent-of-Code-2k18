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

def distance_from_origin(point):
    return np.sum(np.abs(point))

def in_range_nanobots(point):
    points = np.sum(np.abs(nanobots - point), axis=1)
    points.resize(len(points), 1)
    return np.sum(points <= distances)

def get_boundaries(nanobots):
    min_max = lambda i: (min(nanobots, key=lambda s: s[i])[i],
                         max(nanobots, key=lambda s: s[i])[i])
    return min_max(0), min_max(1), min_max(2)

def find_best(step, nanobots, ranges):
    value_key = lambda s: -in_range_nanobots(s) + distance_from_origin(s) / 1e9
    xrange, yrange, zrange = ranges
    points =  np.vstack(np.meshgrid(np.arange(*xrange, step),
                                    np.arange(*yrange, step),
                                    np.arange(*zrange, step))).reshape(3,-1).T
    best = np.array(sorted(points, key=value_key))[0] # This part slows down the function a lot!!
    x,y,z = [*best]
    ranges = [(x, x + step), (y, y + step), (z, z + step)]
    return ranges, best

def part_two(nanobots):
    ranges, best = find_best(1e6, nanobots, get_boundaries(nanobots))
    ranges, best = find_best(1e5, nanobots, ranges)
    ranges, best = find_best(1e4, nanobots, ranges)
    ranges, best = find_best(1e3, nanobots, ranges)
    ranges, best = find_best(1e2, nanobots, ranges)
    ranges, best = find_best(1e1, nanobots, ranges)
    return best


#%% Results

if __name__ == "__main__":
    with open("day23_input.txt") as file:
        total = np.array(list(map(split_line, file.readlines())))
    nanobots, distances = np.split(total, [3], 1)
    print("Answer to part 1 is: {}".format(part_one(total)))
    print("Part 2 has not (yet) been completed.")
    part2 = part_two(nanobots)
    print(part2, in_range_nanobots(part2), int(distance_from_origin(part2)))