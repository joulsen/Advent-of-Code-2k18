# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 17:19:58 2018

@author: Supercigar
"""

filepath = "day01_input.txt"

# PART ONE
def partOne(freq):
    with open(filepath) as file:
        for row in file:
            freq += eval(row)
    return freq


# PART TWO
def partTwo(freq):
    seen = set([freq])
    with open(filepath) as file:
        for row in file:
            freq += eval(row)
            if freq in seen:
                return freq
    return freq