# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:30:39 2019

@author: Andreas
"""
from collections import namedtuple
from PIL import Image, ImageColor, ImageDraw, ImageFont
import numpy as np

class Point(namedtuple("Point", "x y")):
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

grid = dict()
with open("day18_input.txt") as IN:
    for y, row in enumerate(IN.readlines()):
        for x, tile in enumerate(row):
            grid[Point(x,y)] = tile

LIM = [max(grid), min(grid)]
OPEN, TREE, LUMBER = '.', '|', '#'
ADJACENT = [Point( 1,0), Point( 1,1), Point( 1,-1), 
                         Point( 0,1), Point( 0,-1),
            Point(-1,0), Point(-1,1), Point(-1,-1)]

def get_adjacent(point):
    adjacent = ""
    for direction in ADJACENT:
        try:
            adjacent += (grid[point + direction])
        except KeyError:
            pass
    return adjacent

def tick(grid):
    next_grid = grid.copy()
    for point, tile in grid.items():
        if tile == OPEN:
            if get_adjacent(point).count(TREE) >= 3:
                next_grid[point] = TREE
        elif tile == TREE:
            if get_adjacent(point).count(LUMBER) >=3:
                next_grid[point] = LUMBER
        elif tile == LUMBER:
            if get_adjacent(point).count(LUMBER) < 1 or (
               get_adjacent(point).count(TREE) < 1):
                next_grid[point] = OPEN
    return next_grid

def grid2string(grid):
    out = ""
    for y in range(LIM[0].y+1):
        for x in range(LIM[0].x):
            out += grid[Point(x,y)]
        out += '\n'
    return out

colors = {OPEN:   "#ffffff",
          TREE:   "#00ff00",
          LUMBER: "#654321"}
def grid2image(grid, label):
    im = Image.new('RGB', (LIM[0].x+20, LIM[0].y+10), "black")
    draw = ImageDraw.Draw(im)
    for y in range(LIM[0].y+1):
        for x in range(LIM[0].x):
            im.putpixel((x,y), 
                        ImageColor.getcolor(colors[grid[Point(x,y)]], "RGB"))
            draw.text((0,LIM[0].y), label, fill="white")
    return im
#%%
gridlog = set()
for i in range(10):
    gridlog.add(grid2string(grid))
    grid = tick(grid)
p1 = grid.copy()
#%%
# Find first repeat
while(True):
    prev_length = len(gridlog)
    grid = tick(grid)
    gridlog.add(grid2string(grid))
    if len(gridlog) == prev_length:
        break
first_repeat = grid.copy()
# Find length of repeat
grid = tick(grid)
pattern_length = 0
while grid != first_repeat:
    grid = tick(grid)
    pattern_length += 1

#%%
# Get extra iterations and make a nice gif
grid = first_repeat
images = []
found = (1000000000 % (pattern_length - 1)) - 1
for i in range(found):
    images.append(grid2image(grid, "{:3} + {:.0E}".format(i-found,1000000000)))
    gridlog.add(grid2string(grid))
    grid = tick(grid)
p2 = grid.copy()
# Add a couple of extra frames with the part two
for j in range(4):
    images.append(grid2image(grid, "{:3} + {:.0E}".format(0,1000000000)))
for i in range(pattern_length - i):
    images.append(grid2image(grid, "{:3} + {:.0E}".format(i,1000000000)))
    grid = tick(grid)

images[0].save('day18_output.gif', format='GIF', append_images=images[1:], 
               save_all=True, duration=100, loop=0)
#%%


# RESULTS
p1 = grid2string(p1)
p2 = grid2string(p2)
print("Part one: {}".format(p1.count(TREE) * p1.count(LUMBER)))
print("Part one: {}".format(p2.count(TREE) * p2.count(LUMBER)))