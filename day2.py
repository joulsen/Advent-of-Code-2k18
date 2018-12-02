# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:23:03 2018

@author: Supercigar
"""

# PART ONE
from collections import Counter
def getChecksum(IDs):
    check1 = check2 = 0
    for ID in IDs:
        double = triple = 0
        frequency = Counter(ID).most_common()
        for letter in frequency:
            if letter[1] == 2:
                double = 1
            elif letter[1] == 3:
                triple = 1
        check1 += double
        check2 += triple
    return check1 * check2

# PART TWO
def getCommons(IDs, n_common):
    for ID in IDs:
        for checkID in IDs:
            zipped = list(zip(ID, checkID))
            commons = []
            for row in zipped:
                if row[0] is not row[1]:
                    commons.append(row)
            if len(commons) == n_common:
                for common in commons:
                    zipped.remove(common)
                commons = ""
                for i in zipped:
                    commons += i[0]
                return [ID, checkID, commons]

# Create array of each ID
IDs = []
with open("day2_input.txt") as file:
    for row in file:
        IDs.append(row)

# Answers in console
print("Answer to part one: %d" % (getChecksum(IDs)))
print("Answer to part two: %s" % (getCommons(IDs, 1)[2]))