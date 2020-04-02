# -*- coding: utf-8 -*-
"""
@author: Supercigar

Big thanks to /u/sciyoshi for his solution as i became quite stuck.
It can be found at https://www.reddit.com/r/adventofcode/comments/a7uk3f/2018_day_20_solutions/ec5y3lm/

Outline:
The general idea is that we traverse the path string. When we encounter a char
in 'NESW' we simply update our position and add the nodes and verteces into
a graph (network). When we encounter a | we know we must diverge, and the
following happens:
    * The start position is noted so we may return later
    * An end position is noted so we may return after a later )
When a ( is encountered the start and end positions are pushed onto a stack,
and the current position is sat as a start. When the ) is encountered, the
position is updated to the last end, and the last element of (start, end) in
the stack is retrieved into start and end.
"""

import networkx as nx


network = nx.Graph()
path = open("day20_input.txt").read()[1:-1] #removing ^ and $
directions = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}

pos = {0}                   # Used to keep track of positions
starts, ends = {0}, set()   # Possible start and end positions
stack = []                  # 

for c in path:
    if c in "NESW":
        network.add_edges_from((p, p + directions[c]) for p in pos)
        pos = {p + directions[c] for p in pos}
    elif c == '|':
        ends.update(pos)
        pos = starts
    elif c == '(':
        stack.append((starts, ends))
        starts, ends = pos, set()
    elif c == ')':
        pos.update(ends)
        starts, ends = stack.pop()

lengths = nx.algorithms.shortest_path_length(network, 0)

part1 = max(lengths.values())
part2 = len([length for length in lengths.values() if length >= 1000])

print("Answer to part 1 is: {}".format(part1))
print("Answer to part 2 is: {}".format(part2))
