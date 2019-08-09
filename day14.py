# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 20:33:42 2018

@author: Supercigar
"""

import numpy as np

recipes = 939601
sRecipes = np.array([int(x) for x in list(str(recipes))])


def partOne():
    elf1 = 0
    elf2 = 1
    score = [3, 7]
    while len(score) < recipes + 11:
        new_recipe = map(int, list(str(score[elf1] + score[elf2])))
        score += new_recipe
        elf1 = (elf1 + score[elf1] + 1) % len(score)
        elf2 = (elf2 + score[elf2] + 1) % len(score)
    return score[recipes:recipes+10]




elf1 = 0
elf2 = 0
score = [3, 7]
while not (np.array_equal(sRecipes, score[-7:-1]) or np.array_equal(sRecipes, score[-6:])):
        new_recipe = map(int, list(str(score[elf1] + score[elf2])))
        score += new_recipe
        elf1 = (elf1 + score[elf1] + 1) % len(score)
        elf2 = (elf2 + score[elf2] + 1) % len(score)