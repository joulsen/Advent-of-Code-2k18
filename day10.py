# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:40:08 2018

@author: Supercigar
"""
import re
import numpy as np
from matplotlib import pyplot as plt

points = [line for line in open("day10_input.txt", "r").read().splitlines()]
points = [re.findall(r"(-?\d+)", line) for line in points]
points = np.array(points, dtype=int)
points, velocities = np.split(points, 2, axis=1)

# PART ONE & TWO
step = 0
while len(set(points[:,1])) != 10:
    x = abs(min(points[:,0]))+abs(max(points[:,0]))
    y = abs(min(points[:,1]))+abs(max(points[:,1]))
    points += velocities
    step += 1

fig, ax = plt.subplots(figsize=(4,1))
plt.plot(points[:,0], points[:,1], "rs")
ax.invert_yaxis()
ax.set_title("Advent of Code 2018 \n Day 10 \n Steps = %d s" % (step))

fig.savefig("day10_result.png", dpi=100, bbox_inches='tight')
plt.show()