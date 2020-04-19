# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:18:25 2020

@author: Andreas

Firstly an ascii map is drawn like the example.
This map is later to be filled out by hand.

In order to do this, i have made a small ftdetect and syntax file for vim.
These can be found in the resources folder.
The ftdetect file sets the syntax and sets up the commands:
    <C-S> : Replace all '.' with '~' in visual block (<C-V>)
    <C-F> : Replace all '.' with '|' in visual block.
"""

import numpy as np
import sys

def parse_input(filename):
    clay = set()
    with open(filename, "r") as file:
        for line in file.readlines():
            is_x = (line[0] == 'x')
            fixed, varied = map(lambda s: s[2:], line.split(", "))
            varied = list(map(lambda s: int(s), varied.split("..")))

            fixed = [int(fixed) for i in range(varied[0], varied[1] + 1)]
            varied = list(range(varied[0], varied[1] + 1))

            if is_x:
                clay.update(zip(fixed, varied))
            else:
                clay.update(zip(varied, fixed))
    return clay

def get_min_max(clay):
    min_x, max_x = (min(clay)[0], max(clay)[0])
    min_y, max_y = (0, max(clay, key=lambda i: i[1])[1])
    return min_x, max_x, min_y, max_y

asciimap = {True: '#',
            False: '.'}
def draw_ascii(clay, file):
    min_x, max_x, min_y, max_y = get_min_max(clay)
    for y in np.arange(min_y, max_y + 1):
        for x in np.arange(min_x, max_x + 1):
            if (x,y) == (500,0):
                print('+', end='', file=file)
            else:
                print(asciimap[(x,y) in clay], end='', file=file)
        print(file=file)


if __name__ == "__main__":
    draw_ascii(parse_input("day17_input.txt"), open("day17_output.txt", 'w'))