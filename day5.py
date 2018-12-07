# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 22:51:08 2018

@author: Supercigar
"""

import time

# Newline ruined my life
polymer = (open("day5_input.txt", "r")).read().splitlines()[0]


# PART ONE
def reactStringOnce(string):
    for i in range(26):
        string = string.replace(chr(i+65) + chr(i+97), "")
        string = string.replace(chr(i+97) + chr(i+65), "")
    return string


def reactStringFully(string):
    prev = string
    string = reactStringOnce(string)
    while prev != string:
        prev = string
        string = reactStringOnce(string)
    return len(string)

# PART TWO
def getShortestByLetterRemoval(string):
    scores = {}
    for i in range(26):
        test = string.replace(chr(i+65),"")
        test = test.replace(chr(i+97),"")
        scores[chr(i+65)+chr(i+97)] = reactStringFully(test)
    return sorted(scores.items(), key=lambda t: t[1])[0]


# RESULTS
calcTimes = [time.time(), 0, 0]
print("Answer to part one is: %d" % reactStringFully(polymer))
calcTimes[1] = time.time()
print("Answer to part two is: %d" % (getShortestByLetterRemoval(polymer)[1]))
calcTimes[2] = time.time()
print("Calulation times are: %f and %f seconds" % (calcTimes[1]-calcTimes[0],calcTimes[2]-calcTimes[0]))
