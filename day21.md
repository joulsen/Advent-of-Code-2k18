# Advent of code 2018

## Day 21

This uses the same system presented in day 16 and day 19.

### Part 1

In part 1 I must find the lowest value for register 0 such that the program stops executing with the fewest instructions executed. First I present my input:

```
Line   Opcode   Register/Value   Register/Value   Output-register
0      seti     123              0                4
1      bani     4                456              4
2      eqri     4                72               4
3      addr     4                5                5
4      seti     0                0                5
5      seti     0                0                4
6      bori     4                65536            3
7      seti     4332021          4                4
8      bani     3                255              2
9      addr     4                2                4
10     bani     4                16777215         4
11     muli     4                65899            4
12     bani     4                16777215         4
13     gtir     256              3                2
14     addr     2                5                5
15     addi     5                1                5
16     seti     27               5                5
17     seti     0                2                2
18     addi     2                1                1
19     muli     1                256              1
20     gtrr     1                3                1
21     addr     1                5                5
22     addi     5                1                5
23     seti     25               2                5
24     addi     2                1                2
25     seti     17               3                5
26     setr     2                7                3
27     seti     7                1                5
28     eqrr     4                0                2
29     addr     2                5                5
30     seti     5                6                5

```

It seems that the program continues in the loop below, after it reaches line 18 once.

```
18 > 19 > 20 > 21 > 22 > 24 > 25
```

Before performing the first execution of line 18, the registers is as follows, where reg0 is free.

```
[reg0, 0, 0, 65536, 11521639, 17]
```

The register reg0 is free, as before the first execution of line 18, register 0 is never written to or read from. In fact, the only reference to reg0 is on line 28. In order to break the loop we must understand what happens in the loop. Below is some pseudocode:

```
:start
reg1 += reg2 + 1
reg1 *= 256
reg1 = (reg1 > reg3)
if reg1:
	
else:
	
```

