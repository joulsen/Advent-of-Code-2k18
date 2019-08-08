# -*- coding: utf-8 -*-
"""
Created on  Dec 15 15:17:33 2018
Modified on Aug 08 15:56:16 2019

@author: Supercigar
"""

from anytree import Node, findall

data = [int(i) for i in open("day08_input.txt", "r").read().split()]


def makeTree(data, i=0, parent=None):
    node = Node(0, parent=parent)
    nMeta = data[i+1]
    nChild = data[i]
    for c in range(nChild):
        i = makeTree(data, i=i+2, parent=node)
    for m in range(nMeta):
        if not nChild:
            node.name += data[2+i+m]
        else:
            try:
                node.name += node.children[data[2+i+m]-1].name
            except IndexError:
                pass
    for m in range(nMeta): # Doing 2 for-loops to prevent finding new meta-nodes in previous
        Node(data[2+i+m], parent=node)
    if node.is_root: return node
    else:            return i+nMeta


def sumMeta(tree):
    return sum(node.name for node in findall(tree, lambda node: len(node.children) == 0))


# RESULTS
tree = makeTree(data)
print("Part one: {0}".format(sumMeta(tree)))
print("Part two: {0}".format(tree.name))
