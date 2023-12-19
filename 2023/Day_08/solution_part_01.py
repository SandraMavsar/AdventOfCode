# --- Day 8: Haunted Wasteland ---

def part_one():
    steps_required = 0
    position = "AAA"
    index = 0
    while position != "ZZZ":
        move = instructions[index]
        if move == "R":
            position = network[position][1]
            steps_required += 1
        else:
            position = network[position][0]
            steps_required += 1
        index += 1
        if index == len(instructions):
            index = 0
    return steps_required

with open('input.txt') as f:
    lines = f.read().strip().splitlines()

instructions = lines[0]
network = {}

for node in lines[2:]:
    network[node[0:3]] = [node[7:10], node[12:-1]]

print("Part One: ", part_one())

