# --- Day 5: Supply Stacks ---
import re

def part_one(segment, stacks):
    crates_to_move = stacks[segment[1]][(len(stacks[segment[1]]) - segment[0]):]
    for i in reversed(crates_to_move):
        stacks[segment[2]] += i
        stacks[segment[1]] = stacks[segment[1]][:-1]
    return stacks

def part_two(segment, stacks2):
    crates_to_move = stacks2[segment[1]][(len(stacks2[segment[1]]) - segment[0]):]
    stacks2[segment[2]] += crates_to_move
    for i in crates_to_move:
        stacks2[segment[1]] = stacks2[segment[1]][:-1]
    return stacks2

data, lines = open('input.txt').read().split("\n\n")
stacks = [
    "".join(column).rstrip()
    for i, column in enumerate(zip(*data.splitlines()[-2::-1]))
    if i % 4 == 1
]
stacks2 = stacks.copy()

rules = re.findall(r"\d+", lines)
j = 3
while j <= len(rules):
    segment = rules[j - 3:j]
    segment = [int(segment[0]), int(segment[1]) - 1, int(segment[2]) - 1]
    part_one(segment, stacks)
    part_two(segment, stacks2)
    j += 3

solution = ''; solution2 = ''
for i in stacks:
    solution += i[-1]

for i in stacks2:
    solution2 += i[-1]

print('Part One: ', solution)
print('Part Two: ', solution2)
