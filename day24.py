# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:51:20 2020

@author: Andreas
"""

ARMIES = 2
team = {0: "   Immune",
        1: "Infection"}

import re
from math import ceil
interpreter = re.compile(r"(?P<size>\d+) units each with (?P<hp>\d+) hit points \(?(?P<modifiers>.+?)?\)? ?with an attack that does (?P<atk>\d+) (?P<atk_type>\w+) damage at initiative (?P<initiative>\d+)")

def parse_input():
    with open("day24_input.txt") as file:
        it = interpreter.finditer(file.read())
    armies = list(map(lambda a: a.groupdict(), it))
    for i, army in enumerate((armies)):
        # Dividing into teams
        if i < ARMIES:
            army["team"] = 0 # 0 is immune system
        else:
            army["team"] = 1 # 1 is infection
        army["id"] = i
        army["number"] = (i % ARMIES) + 1
        # Dividing into weaknesses and immunities
        if army["modifiers"] is not None:
            try:
                army["immunity"], army["weakness"] = army["modifiers"].split("; ")
            except ValueError:
                if "immune" in army["modifiers"]:
                    army["immunity"] = army["modifiers"]
                    army["weakness"] = ""
                elif "weak" in army["modifiers"]:
                    army["weakness"] = army["modifiers"]
                    army["immunity"] = ""
        else:
            army["weakness"], army["immunity"] = ["", ""]
        army["targeted"] = False
        # Creating integers.
        for key, value in army.items():
            if key in ["atk", "size", "hp", "initiative"]:
                army[key] = int(value)
    return armies

def update_ep():
    for army in armies:
        army["ep"] = army["atk"] * army["size"]

def sort_by_ep():
    return sorted(armies, key = lambda a: -a["ep"] - a["initiative"] / 2*ARMIES)

def sort_by_initiative():
    return sorted(armies, key = lambda a: -a["initiative"])

def find_target(attacker):
    enemies = [e for e in sort_by_ep() if e["id"] != attacker["id"] and e["team"] != attacker["team"] and e["targeted"] is False]
    optimal = None
    for enemy in enemies:
        if attacker["atk_type"] in enemy["weakness"]:
            optimal = enemy
            break
        elif (optimal is None and attacker["atk_type"] not in enemy["immunity"]):
            optimal = enemy
    if optimal is None:
        print("{} group #{} cannot find a target.".format(team[attacker["team"]], attacker["number"]))
        attacker["target"] = None
        return None
    else:
        print("{} group #{} targets enemy #{}".format(team[attacker["team"]], attacker["number"], optimal["number"]))
        attacker["target"] = optimal
        enemy["targeted"] = True
        return optimal

def attack(attacker):
    if attacker["target"] != None:
        dmg = attacker["atk"] * attacker["size"]
        enemy = attacker["target"]
        if attacker["atk_type"] in enemy["weakness"]:
            dmg *= 2
        hp_after = enemy["size"] * enemy["hp"] - dmg
        units_before = enemy["size"]
        enemy["size"] = ceil(hp_after / enemy["hp"])
        if enemy["size"] < 0:
            enemy["size"] = 0
        print("{} group #{} attacks enemy #{} for {} dmg, killing {} units and leaving {}.".format(team[attacker["team"]], attacker["number"], enemy["number"], 
                                                                                                dmg, units_before - enemy["size"], enemy["size"]))
        return 1
    else:
        return 0

def turn():
    update_ep()
    armies = sort_by_ep()
    for army in armies:
        find_target(army)
    armies = sort_by_initiative()
    attacked = 0
    for army in armies:
        attacked += attack(army)
    new_armies = []
    for army in armies:
        if army["size"] > 0:
            army["targeted"] = False
            new_armies.append(army)
    print("")
    return new_armies, (attacked > 0)

armies = parse_input()
while(True):
    armies, attacked = turn()
    if attacked == 0:
        break
print("Answer to part 1 is: {}".format(sum([a["size"] for a in armies])))

for army in armies:
    print(army["size"])