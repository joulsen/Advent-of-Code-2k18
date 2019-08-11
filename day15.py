# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 20:36:10 2019

@author: Andreas
"""

import numpy as np
grid = np.array([list(line) for line in open("day15_input.txt", "r").read().splitlines()])

class Unit:
    def __init__(self, pos, name):
        self.hp = 200
        self.atk = 3
        self.pos = np.array(pos)
        self.name = name
        self.alive = True

    def inRange(self):
        if self.name == "Elf":      unit_list = goblins
        elif self.name == "Goblin": unit_list = elves
        unit_pos = np.stack([unit.pos for unit in unit_list], axis=1)[0]
        relative = unit_pos - self.pos
        dists = np.linalg.norm(relative, axis=1)
        inRange = (dists == 1)
        return unit_list[inRange]

    def attack(self, targetable):
        target = sorted(targetable, key=lambda u: u.hp)[0]
        target.hp -= self.atk
        print(self.name, "at", self.pos, "attacks", target.name, "at", target.pos, "for", self.atk, "damage")
        if target.hp < 0:
            print(self.name, "at", self.pos, "slays  ", target.name, "at", target.pos)
            target.alive = False


elves = np.array([Unit([coord], "Elf") for coord in np.argwhere(grid == 'E')])
goblins = np.array([Unit([coord], "Goblin") for coord in np.argwhere(grid == 'G')])
units = np.concatenate((elves, goblins), axis=0)
walls = [coord for coord in np.argwhere(grid=='#')]


def getByName(unit_list, name):
    return 

def sortTurn(units):
    return np.array(sorted(units, key=lambda u: u.pos[0][0] + u.pos[0][1] / 10))





"""
class Elf(Unit):
    def __init__(self, pos):
        super(Elf, self).__init__(pos)
        self.name = 'Elf'
"""