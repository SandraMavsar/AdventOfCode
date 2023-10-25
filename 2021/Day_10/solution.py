# --- Day 10: Syntax Scoring ---

with open('input.txt') as f:
    data = f.read().split("\n")

print(data)

for line in data:
    open = {"(": 0, "[": 0, "{": 0, "<": 0}
    closed = {")": [0, "("], "]": [0, "["], "}": [0, "{"], ">": [0, "<"]}
    illegal = {")": 3, "]": 57, "}": 1197, ">": 25137}
    illegal_count = 0
    for character in line:
        if character in open:
            open[character] += 1
        else:
            closed[character][0] += 1
            if closed[character][0] > open[closed[character][1]]:
                illegal_count += illegal[character]
                break

print(illegal_count)