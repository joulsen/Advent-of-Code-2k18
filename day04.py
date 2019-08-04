# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 19:49:53 2018

@author: Supercigar
"""

import re
from collections import Counter
file = open("day04_input.txt")
file = file.readlines()
file.sort()


# PART ONE
def makeRegister(file):
    register = {}
    for line in file:
        if "Guard" in line:
            guardID = int((re.search(r'#(\d+)', line)).group(1))
        if "asleep" in line:
            t0 = int(line[15:17])
        elif "wakes" in line:
            try:
                register[guardID].update(range(t0, int(line[15:17])))
            except KeyError:
                register[guardID] = Counter(range(t0, int(line[15:17])))
    return register


def mostSleepy(register):
    return sorted(register, key=lambda x: -sum(register[x].values()))[0]


def partOne(register):
    guardID = mostSleepy(register)
    minute = register[guardID].most_common(1)[0][0]
    return "{0} * {1} = {2}".format(guardID, minute, guardID*minute)


# PART TWO
def mostFrequent(register):
    return sorted(register, key=lambda x: -register[x].most_common(1)[0][1])[0]


def partTwo(register):
    guardID = mostFrequent(register)
    minute = minute = register[guardID].most_common(1)[0][0]
    return "{0} * {1} = {2}".format(guardID, minute, guardID*minute)


# Results
register = makeRegister(file)
print(partOne(register))
print(partTwo(register))
