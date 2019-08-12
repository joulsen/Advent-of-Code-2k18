# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 17:48:44 2019

@author: Andreas
"""

from collections import Counter, defaultdict

# Annoying format this time around. Couldn't be bothered with regex.
file = open("day16_input.txt").read()
samples = file[:file.find("\n\n\n")].replace("Before: [","").replace("After:  [","").replace("]","").replace(", "," ").replace("\n\n", "\n").split('\n')
samples = list(map(lambda s: list(map(int, s.split(" "))), samples))
program = file[file.find("\n\n\n")+4:-1].split('\n')
program = list(map(lambda s: list(map(int, s.split(" "))), program))

# OPCODES
def addr(r, o): r[o[3]] = r[o[2]] + r[o[1]]
def addi(r, o): r[o[3]] = o[2] + r[o[1]]
def mulr(r, o): r[o[3]] = r[o[2]] * r[o[1]]
def muli(r, o): r[o[3]] = o[2] * r[o[1]]
def banr(r, o): r[o[3]] = r[o[2]] & r[o[1]]
def bani(r, o): r[o[3]] = o[2] & r[o[1]]
def borr(r, o): r[o[3]] = r[o[2]] | r[o[1]]
def bori(r, o): r[o[3]] = o[2] | r[o[1]]
def setr(r, o): r[o[3]] = r[o[1]]
def seti(r, o): r[o[3]] = o[1]
def gtir(r, o): r[o[3]] = int((o[1] > r[o[2]]))
def gtri(r, o): r[o[3]] = int((r[o[1]] > o[2]))
def gtrr(r, o): r[o[3]] = int((r[o[1]] > r[o[2]]))
def eqir(r, o): r[o[3]] = int((o[1] == r[o[2]]))
def eqri(r, o): r[o[3]] = int((r[o[1]] == o[2]))
def eqrr(r, o): r[o[3]] = int((r[o[1]] == r[o[2]]))
funcs = [addr, addi, mulr, muli,
         banr, bani, borr, bori,
         setr, seti, gtir, gtri,
         gtrr, eqir, eqri, eqrr]


translationDict = defaultdict(set)
plus2 = 0
for i in range(0, len(samples), 3):
    before, op, after = samples[i:i+3]
    like = set()
    for func in funcs:
        t = before.copy()
        func(t, op)
        if t == after:
            like.add(func)
            translationDict[op[0]].add(func)
    if len(like) > 2:
        plus2 += 1

isolated = []
while(len(isolated) != len(funcs)):
    isolated = [list(x)[0] for x in translationDict.values() if len(x) == 1]
    for func in isolated:
        for key in translationDict:
            try:
                if len(translationDict[key]) > 1:
                    translationDict[key].remove(func)
            except KeyError:
                pass

for key, value in translationDict.items():
    translationDict[key] = list(value)[0]

reg = [0,0,0,0]
for line in program:
    translationDict[line[0]](reg, line)

# Results
print("Part one:", plus2)
print("Part two:", reg[0])