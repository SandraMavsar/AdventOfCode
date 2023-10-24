# --- Day 2: Dive! ---

import re
def part_one():
    position = {"f": 0, "d": 0, "u": 0}
    for i in data:
        number = int(re.search(r'\d+', i).group())
        position[i[0]] += number

    return position["f"] * (position["d"] - position["u"])

def part_two():
    position = {"f": 0, "d": 0}
    aim = 0
    for i in data:
        number = int(re.search(r'\d+', i).group())
        if i[0] == "d":
            aim += number
        elif i[0] == "u":
            aim -= number
        else:
            position["f"] += number
            position["d"] += number * aim

    return position["f"] * position["d"]


with open('input.txt') as f:
    data = f.read().split("\n")

print("Part One: ", part_one())
print("Part Two: ", part_two())