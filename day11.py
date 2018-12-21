# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:15:04 2018

@author: Supercigar
"""
import numpy as np
serial = 5153


def createGrid(serial):
    grid = np.zeros([300, 300], dtype=int)
    basepwr = np.array([i+1 for i in range(300)])
    for row in range(len(grid)):
        grid[row] += basepwr+10
        grid[row] *= row + 1
        grid[row] += serial
        grid[row] *= basepwr+10
        grid[row] = (list(map(lambda x: int(str(x)[-3]), grid[row])))
        grid[row] -= 5
    return grid


# PART ONE
def getLargest3x3(grid, size):
    grid = createGrid(serial)
    lx = ly = lc = -1000000000
    for y in range(len(grid)-(size-1)):
        for x in range(len(grid)-(size-1)):
            cell = np.sum(grid[y:y+size, x:x+size])
            if cell > lc:
                lc = cell
                lx = x + 1
                ly = y + 1
    return (lx, ly), lc


# PART TWO
grid = createGrid(5153)
bCoord = bValue = bSize = 0
for size in range(1,20):
    coord, value = getLargest3x3(grid,size)
    if value > bValue:
        bValue = value
        bCoord = coord
        bSize = size


# RESULTS
print("Answer to part one is: {0}".format(getLargest3x3(createGrid(5153),3)[0]))
print("Answer to part one is: {0},{1},{2}".format(bCoord[0], bCoord[1], bSize))