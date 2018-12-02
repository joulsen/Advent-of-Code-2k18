# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:23:03 2018

@author: Supercigar
"""

# PART ONE
from collections import Counter
def getChecksum(IDs):
    check = [0,0]
    for ID in IDs:
        counts = [count for i,count in Counter(ID).most_common()]
        if 3 in counts:
            check[0] += 1
        if 2 in counts:
            check[1] += 1
    return check[0] * check[1]
    
# PART TWO
from itertools import combinations
def getCommons(IDs, n_common):
    for comparison in combinations(IDs,2):
        commons = ""
        for ID, cID in [comparison]:
            for i in range(len(ID)):
                if ID[i] == cID[i]:
                    commons += ID[i]
            if len(commons) == len(ID) - n_common:
                return commons

# Create array of each ID
IDs = []
with open("day2_input.txt", 'r') as file:
    for row in file:
        IDs.append(row)

# Answers in console
print("Answer to part one: %d" % (getChecksum(IDs)))
print("Answer to part two: %s" % (getCommons(IDs, 1)))