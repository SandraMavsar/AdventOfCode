# --- Day 8: Haunted Wasteland ---

import re
import math
import collections


with open('input.txt') as f:
    lines = f.read().strip().splitlines()

directions = lines[0].strip()
m = {}
for line in lines[2:]:
    place, left, right = re.findall("\w+", line)
    m[place] = (left, right)

# Part 2: Calculate distances to 'Z' for places ending with 'A'
steps_to_z = collections.defaultdict(list)

def calculate_distance(place):
    original_place = place
    visited = set()
    steps = 0
    i = -1
    while True:
        if place[-1] == 'Z':
            steps_to_z[original_place].append(steps)
        steps += 1
        i = (i + 1) % len(directions)
        move = directions[i]
        state = (place, i)
        if state in visited:
            break
        visited.add(state)
        if move == 'L':
            place = m[place][0]
        else:
            place = m[place][1]

# Calculate distances for places ending with 'A'
for place in m:
    if place[-1] == 'A':
        calculate_distance(place)

# Find the least common multiple of the distances
all_distances = set()
for place in m:
    if place[-1] == 'A':
        all_distances |= set(steps_to_z[place])

result = math.lcm(*list(all_distances))

print("Part Two:", result)
