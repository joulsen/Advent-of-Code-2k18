# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 20:36:10 2019

@author: Andreas
"""

import numpy as np
file = np.array([list(line) for line in open("day15_input.txt", "r").read().splitlines()])

class Soldier:
    def __init__(self, type, pos):
        self.type = type
        self.pos = pos