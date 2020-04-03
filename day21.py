# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 21:58:44 2020

@author: Andreas
"""

#%% Edited from day19.py
def lazy2int(i):
    try:
        return int(i)
    except ValueError:
        return i


with open("day21_input.txt") as IN:
    program = list(map(lambda s: list(map(lazy2int,
                                          s.split(" "))), IN.readlines()))
    ip_register = program[0][1]
    program.pop(0)  # Removing ip declaration, such that index matches ip.


# OPCODES from day16
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
# Making a dictionary for easier calling from string
funcs = {func.__name__: func for func in funcs}


def doProgram(reg, program, max_steps = 45):
    ip = 0
    executions = 0
    while 0 <= ip < len(program) and executions < max_steps:
        print(reg)
        print(ip, program[ip])
        reg[ip_register] = ip
        funcs[program[ip][0]](reg, program[ip])
        ip = reg[ip_register]
        ip += 1
        executions += 1
    return reg

#%% New

doProgram([0,0,0,0,0, 0], program)