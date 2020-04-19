# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:25:53 2020

@author: Andreas

This program converts the ascii map to a png image.
"""

from PIL import Image, ImageDraw

file = open("day17_output.day17", "r").read().split('\n')
img = Image.new('RGB', (len(file[0]), len(file)))
draw = ImageDraw.Draw(img)

colors = {'.': "white",
          '#': "gray",
          '|': "cyan",
          '~': "blue",
          '+': "green"}

for y, line in enumerate(file):
    for x, char in enumerate(line):
        draw.point((x, y), colors[char])

img.save("day17_output.png")