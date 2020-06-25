# -*- coding: utf-8 -*-
"""
Created on 25-06-2020 22:51:20
@author: Andreas
"""
import csv
from collections import deque
from itertools import chain

with open("day25_input.txt") as file:
    reader = csv.reader(file)
    points = list([list(map(int, x)) for x in reader])

def dist(p1, p2):
    return sum([abs(p2[n] - p1[n]) for n in range(4)])

def in_constellation(constellation, p):
    for point in constellation:
        if dist(point, p) <= 3:
            return True
    return False

def same_constellation(c1, c2):
    for point in c1:
        if in_constellation(c2, point):
            return True
    return False

def form_constellations(points):
    constellations = deque()
    for point in points:
        match = False
        for constellation in constellations:
            match = in_constellation(constellation, point)
            if match:
                constellation.append(point)
                break
        constellations.append([point])
    return constellations

constellations = form_constellations(points)

def merge_constellations(constellations):
    c1 = constellations.popleft()
    sub_constellations = deque(c1)
    for i in range(len(constellations)):
        c2 = constellations.popleft()
        if same_constellation(c1, c2):
            sub_constellations.extend(c2)
        else:
            constellations.append(c2)
    constellations.append(sub_constellations)
    if sub_constellations == deque(c1):
        return False
    else:
        return True

while sum([merge_constellations(constellations) for i in range(len(constellations))]) != 0:
    pass

print("Answer to part 1 is {}".format(len(constellations)))