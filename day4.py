# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 19:49:53 2018

@author: Supercigar
"""

import re
import datetime as dt
with open("day4_input.txt", 'r') as file:
    log = []
    for row in file:
        date = [int(i) for i in re.findall(r"\d+", row)]
        #log.append(date)
        date = dt.datetime(*tuple(date[0:5]))
        log.append([date, (re.findall(r"(asleep|wakes|#\d+)", row))[0]])
        log.sort()
del row, date

# PART ONE
from collections import defaultdict, Counter
time_slept = defaultdict(int)
distribution = defaultdict(Counter)
cID = None
for i in range(len(log)):
    if log[i][1][0] == "#":
        cID = log[i][1]
    elif log[i][1] == "asleep":
        asleep = log[i][0]
        awake = log[i+1][0]
        time_slept[cID] += int((awake - asleep).total_seconds() / 60)
        distribution[cID].update([i for i in range(asleep.minute, awake.minute)])
resident_sleeper = [0, max([slept for ID,slept in time_slept.items()]), 0]
for i,x in time_slept.items():
    if x == resident_sleeper[1]:
        resident_sleeper[0] = i
resident_sleeper[2] = distribution[resident_sleeper[0]].most_common()[0][0]
result = resident_sleeper[1] * resident_sleeper[2]
'''
for i,x in time_slept.items():
    lol = max([x for i,x in time_slept.items()])
    if x == lol:
        print(i)

from collections import defaultdict, Counter
from numpy import arange
time_slept = defaultdict(int)
minutes_asleep = defaultdict(Counter)
cID = None
for i in range(len(log)):
    if log[i][1][0] == "#":
        cID = log[i][1]
    elif log[i][1] == "asleep":
        slept = int((log[i+1][0] - log[i][0]).total_seconds() / 60)
        time_slept[cID] += slept
        for i in range(slept):
            minutes_asleep[cID][i+log[i][0].minute] += 1

from collections import defaultdict
sleepy = defaultdict(int)
cID = None
for i in range(len(log)):
    try:
        cID = log[i][0][5]
        print(cID)
    except IndexError:
        if log[i][1] == "asleep":
            sleepy[cID] += log[i][0]

'''