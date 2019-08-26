# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 19:07:18 2019

@author: Supercigar
"""


def lazy2int(i):
    try:
        return int(i)
    except ValueError:
        return i


with open("day19_input.txt") as IN:
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


def doProgram(reg, program):
    ip = 0
    while 0 <= ip < len(program):
        reg[ip_register] = ip
        funcs[program[ip][0]](reg, program[ip])
        ip = reg[ip_register]
        ip += 1
    return reg


"""
- - - PART TWO - - -
This part of the exercise seems to be meant for reverse-engineering, which i
will promptly attempt. Remember that this may only be the case for my specific
input, and may not work if you attempt the same.

I see that the program loops seemingly indefinitely for reg = [1, 0, 0, ...]
The IP goes in loop: ... 3, 4, 5, 6, 8, 9, 10, 11, 3, 4 ...
Furthermore, before entering the loop the register tells
[0, 10551292, 2, 1, 10550400, 1] just before opcode 3

Definition, for later use:
OPCODE INNER LOOP  OUTER LOOP
1      -----       -----
2          |           |
3          |           |
4          |           |
5          |           |
6          |           |
7          |           |
8          |           |
9          |           |
10         |           |
11     -----           |
12                     |
13                     |
14                     |
15                 -----
16

The program seems to work like so:
Firstly, R1 and R4 are set to large numbers and R1 > R4 (10551292 > 10550400)
Then the loop 3-11 adds 1 to R3 each iteration.
Interestingly in the loop:
    * R1 and R5 remain constant
    * R3 increases by 1 with each iteration
    * R2 and R4 are the same at the beginning of each iteration
    * When (R1 == R3 * R5): R0 += R5
    (This effectively means, that R0 only increases when (R1 % R3 == 0) or
    (R1 % R5 == 0))
    * When (R3 > R1): The loop is broken and continues to opcode 12
From opcode 12 the following happens:
    * R5 increases by 1
    * If (R5 > R1): Go back to loop and reset R3
If this if-condition is not met, the program will execute opcode 16, which
always halts the program.

In order for the program to terminate, R5 must be larger than R1 which happens
after getting past opcode 12 R1 times. But getting through R1 requires going
through the loop 3-11 R1 times aswell. Therefore, the inner loop of 3-11 exe-
cutes a total of R1^2 times (1.113298E+14).

We are interested in R0, which only changes when the inner-loop counter R3 and
the outer-loop counter R5 multiplied gives R1. This can only happen once per
outer loop. Furthermore, this only happens when (R1 % R3 == 0) and
(R1 % R5 == 0). We see that, since R1 is an even number 10551292, if R3 is odd,
R0 will not increase in that outer-loop iteration.

We can now write something equivalent:
    For every number j from 1 to 10551292, R0 is equal to the accumulation of
    j if (10551292 % j == 0).
"""

R0 = 0
R1 = 10551292
for i in range(1, R1+1):
    if not (R1 % i):
        R0 += i

print("Part one: {}".format(doProgram([0, 0, 0, 0, 0, 0], program)[0]))
print("Part two: {}".format(R0))
