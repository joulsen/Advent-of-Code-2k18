# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 19:13:02 2018

@author: Supercigar
"""
import re
import numpy as np
orders = [re.findall(r"^Step ([A-Z]) must be finished before step ([A-Z]) can begin.$", line)[0] for line in open("day07_input.txt", "r").readlines()]
orders = [tuple(map(lambda x : ord(x)-65, order)) for order in orders]

# PART ONE
def getGrid(orders):
    grid = np.zeros(shape=[26,26])
    for order in orders:
        grid[order[1]][order[0]] = 1
    return grid

def getChoices(grid, solution, n=1, clear=True):
    choices = []
    for row in range(len(grid)):
        if np.sum(grid[row]) == 0:
            choices.append(row)
    new = choices.copy()
    for choice in choices:
        if chr(choice+65) in solution:
            new.remove(choice)
    new.sort()
    if clear is True:
        grid[:,new[0]] = 0
    #solution += chr(new[0]+65)
    return grid, new[0:n]

def partOne(orders):
    grid = getGrid(orders)
    solution = ""
    while len(solution) != 26:
        grid, choice = getChoices(grid, solution)
        solution += chr(choice[0]+65)
    return solution

# PART TWO
def partTwo(orders, workers, joblength):
    grid = getGrid(orders)
    solution = premature = ""
    current = []
    timer = []
    step = 0
    while len(solution) != 26:
        choices = getChoices(grid, premature, workers-len(current), False)[1]
        for choice in choices:
            if not choice in current:
                #print("Starting %s at %d" % (chr(choice+65), step))
                current.append(choice)
                timer.append(choice+joblength+1)
                premature += chr(choice+65)
        while min(timer) != 0:
            timer = [time-1 for time in timer]
            step += 1
        for time in range(len(timer)):
            if timer[time] == 0:
                #print("Finished %s at %d" % (chr(current[time]+65), step))
                grid[:,current[time]] = 0
                solution += chr(current[time]+65)
                timer.pop(time)
                current.pop(time)
                break
    return step

# RESULTS
print("Answer to part one is: %s" % partOne(orders))
print("Answer to part one is: %d" % partTwo(orders, 5, 60))