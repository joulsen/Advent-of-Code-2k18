# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 18:17:57 2020

@author: Andreas
"""

# Imports
from matplotlib import pyplot as plt
from collections import deque
import numpy as np
import operator

def add(a, b):
    return tuple(map(operator.add, a, b))

def parseInput(filename):
    clay = set()
    with open(filename, "r") as file:
        for line in file.readlines():
            is_x = (line[0] == 'x')
            fixed, varied = map(lambda s: s[2:], line.split(", "))
            varied = list(map(lambda s: int(s), varied.split("..")))
    
            fixed = [int(fixed) for i in range(varied[0], varied[1] + 1)]
            varied = list(range(varied[0], varied[1] + 1))
    
            if is_x:
                clay.update(zip(fixed, varied))
            else:
                clay.update(zip(varied, fixed))
    return clay


def plot(data):
    fig, ax = plt.subplots()
    ax.invert_yaxis()
    for set in data:
        x = [c[0] for c in set]
        y = [c[1] for c in set]
        plt.plot(x, y, "s")

clay = parseInput("day17_example.txt")
flowing = deque()
flowing.append((500,0)) # Initial water source

current = flowing.pop()
while True:
    current = add(current, (0,1))
    flowing.append(current)
    if add(current, (0,1)) in clay:
        break


plot([clay])