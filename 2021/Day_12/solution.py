# --- Day 12: Passage Pathing ---

# Solved with the help from Reddit, not 100% my solution.

"""
Solved with the help from Reddit, not 100% my solution.
Depth-First Search (DFS) is an algorithm for traversing or searching tree or graph data structures.
It starts at the root (selecting some arbitrary node as the root in the case of a graph) and explores as far as
possible along each branch before backtracking. DFS does not guarantee the shortest path to a
goal, but it's often used when you want to explore all possible paths and discover all connected components in
a graph or tree.

Steps:
1. Start at the Root: Begin at the starting node (the root of the tree or a specified starting point in a graph).
2. Visit the Node: Mark the current node as visited. This could involve various operations depending on the specific
problem or application.
3. Explore Unvisited Neighbors: Go to an unvisited neighbor of the current node. If there are multiple unvisited
neighbors, you can choose any of them (the order might affect the search path).
4.Repeat the Process: If there are unvisited neighbors, repeat the process starting from the new neighbor. This step is
recursive in nature, which allows DFS to explore deeply into the graph before backtracking.
5 Backtrack: When you reach a node with no unvisited neighbors, backtrack to the previous node
(the one that led to the current node). If there are other unexplored branches, explore those.
6 Repeat Until Complete: Continue this process until you have visited all nodes that are reachable
from the starting point.
"""

with open('input.txt') as f:
    data = f.read().split("\n")


from collections import defaultdict
#   module to create a dictionary where the values are lists.
#   It is used to build a graph of neighbors based on the input data.
neighbours = defaultdict(list)

for line in data:
    a, b = line.strip().split('-')
    neighbours[a] += [b]
    neighbours[b] += [a]


def count(part, seen=[], cave='start'):
    if cave == 'end':
        return 1
    if cave in seen:
        if cave == 'start':
            return 0
        if cave.islower():
            if part == 1:
                return 0
            else:
                part = 1
    new = seen + [cave]
    return sum(count(part, new, n)
                for n in neighbours[cave])


print("Part One: ", count(part=1))
print("Part Two", count(part=2))


