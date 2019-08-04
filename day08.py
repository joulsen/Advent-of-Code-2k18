# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 15:17:33 2018

@author: Supercigar
"""
from anytree import Node, RenderTree
import pdb
data = [int(i) for i in open("day08_input.txt", "r").read().split()]

# PART ONE
def partOne(parent = None, first = True):
    if first:
        global mdsum, ce
        mdsum = ce = 0
    cN_children = data[ce]
    cN_metanums = data[ce+1]
    ce += 2
    cN = Node("%d|%d" % (cN_children, cN_metanums), parent=parent)
    for i in range(cN_children):
        child = partOne(cN, False)
    for number in range(cN_metanums):
        mdsum += data[ce]
        ce += 1
    return cN

# PART TWO


# RESULTS
cN = partOne()
print("Answer to part one is: %d" % mdsum)