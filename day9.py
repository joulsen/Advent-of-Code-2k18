# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 18:26:05 2018

@author: Supercigar
"""
from collections import deque
from time import time
parameters = [int(i) for i in open("day9_input.txt", "r").read().split() if i.isdigit()]

# PART ONE & TWO
def playGame(players, highest):
    scores = [0 for i in range(players)]
    circle = deque([0])
    for i in range(1,highest+1):
        cp = (i-1) % players
        if i % 23 == 0:
            circle.rotate(7)
            scores[cp] += circle.pop() + i
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(i)
    return max(scores)

# RESULTS
print("Answer to part one is: %d" % playGame(parameters[0],parameters[1]))
print("Answer to part one is: %d" % playGame(parameters[0],parameters[1]*100))