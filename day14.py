# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 20:33:42 2018

@author: Supercigar
"""

data = 939601
recipes = "37"

# PART ONE
elves = [0,1]
def makeRecipe(elves, recipes):
    recipes += str(int(recipes[elves[0]]) + int(recipes[elves[1]]))
    for i in range(len(elves)):
            elves[i] = (int(recipes[elves[i]]) + elves[i] + 1) % len(recipes)
    return elves, recipes

def getScore(elves, recipes, amount, score_buffer = 10):
    elves = elves[:]
    for i in range(amount + score_buffer):
        elves, recipes = makeRecipe(elves, recipes)
    return recipes[amount:amount+score_buffer]

# PART TWO
def partTwo(elves, recipes, score):
    elves = elves[:]
    while(score not in recipes[-len(score):]):
        elves, recipes = makeRecipe(elves, recipes)
    return len(recipes) - len(score)

# Taking too damn long. Needs an optimization

# RESULTS
print("Answer to part one is: {0}".format(makeRecipes(elves, recipes, data)))
