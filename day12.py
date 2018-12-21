# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 18:54:38 2018

@author: Supercigar
"""
from matplotlib import pyplot as plt
file = open("day12_input.txt", "r").read().splitlines()
state = file[0].split()[2]
rules = [rule.split(" => ") for rule in file[2:]]
del file


def pad(string, padding):
    return "." * padding + string + "." * padding


# PART ONE
def replaceN(string, char, n):
    return string[:n] + char + string[n+1:]


def stepGen(state, rules, steps):
    for i in range(steps):
        prev = state
        state = "." * len(prev)
        for rule in rules:
            ns = [i for i in range(len(prev)) if prev.startswith(rule[0], i)]
            for apperance in ns:
                state = replaceN(state, rule[1], apperance+2)
    return state


def calcIndexSum(state, zero):
    ns = [i - zero for i in range(len(state)) if state.startswith("#", i)]
    return sum(ns)


# PART TWO
def showCorrelation(state, zero):
    x = [x for x in range(0, 200, 10)]
    y = [calcIndexSum(stepGen(state, rules, x), zero) for x in x]
    plt.plot(x, y)


def calcIndexSumFF(state, rules, steps, zero):
    rough_lower = calcIndexSum(stepGen(state, rules, 110), zero)
    incline = calcIndexSum(stepGen(state, rules, 111), zero) - rough_lower
    return rough_lower + incline * (steps-110)


# RESULTS
print("Answer to part one is: {0}".format(calcIndexSum(stepGen(pad(state, 22), rules, 20), 22)))
print("Answer to part one is: {0}".format(calcIndexSumFF(pad(state, 113), rules, 50000000000, 113)))
# These paddings were determined as absolute minimums for this input