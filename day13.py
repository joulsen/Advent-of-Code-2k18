# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 20:55:12 2018

@author: Supercigar
"""

from collections import deque, Counter
import numpy as np

file = open("day13_input.txt")
tracks = file.readlines()
directions = '^>v<'
compass = deque(list(directions))
route = deque([1, 0, -1])


class cart:
    def __init__(self, heading, position):
        self.heading = (compass.copy())
        while self.heading[0] != heading:
            self.heading.rotate(1)
        self.position = np.array(position)
        self.route = route.copy()

    def drive(self):
        if   self.heading[0] == '^': self.position += [0, -1]
        elif self.heading[0] == '>': self.position += [1, 0]
        elif self.heading[0] == 'v': self.position += [0, 1]
        elif self.heading[0] == '<': self.position += [-1, 0]

    def turn(self):
        self.heading.rotate(self.route[0])
        self.route.rotate(-1)

    def tick(self):
        character = tracks[self.position[1]][self.position[0]]
        if character == '/':
            if self.heading[0] in '^v':
                self.heading.rotate(-1)
            else:
                self.heading.rotate(1)
        elif character == '\\':
            if self.heading[0] in '^v':
                self.heading.rotate(1)
            else:
                self.heading.rotate(-1)
        elif character == '+':
            self.turn()
        self.drive()


def getCarts(tracks):
    carts = []
    for y in range(len(tracks)):
        for x in range(len(tracks[y])):
            if tracks[y][x] in directions:
                carts.append(cart(tracks[y][x], [x, y]))
    return carts


def cart_sort(x):
    return x.position[1] + (x.position[0] / 10)


def getFirstCrash(tracks):
    carts = getCarts(tracks)
    while True:
        coords = []
        carts.sort(key=cart_sort)
        for cart in carts:
            cart.tick()
            coords.append(str(cart.position))
            if len(coords) != len(set(coords)):
                return Counter(coords).most_common()[0][0]


def getLastCart(tracks):
    carts = getCarts(tracks)
    while True:
        carts.sort(key=cart_sort)
        for cart in carts:
            coords = [str(cart.position) for cart in carts]
            cart.tick()
            coords.append(str(cart.position))
            if Counter(coords).most_common(1)[0][1] > 1:
                crashCoord = Counter(coords).most_common(1)[0][0]
                carts = [cart for cart in carts if str(cart.position) != crashCoord]
                print("Crash at {0}. {1} carts remaining!".format(crashCoord, len(carts)))
                coords = []
        if len(carts) == 1:
            return carts[0].position


# RESULTS
print("Result for the first part is: {0}".format(getFirstCrash(tracks)))
print("Progress of part two:")
print("And the result is: {0}".format(getLastCart(tracks)))
