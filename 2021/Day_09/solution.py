# --- Day 9: Smoke Basin ---

with open('input.txt') as f:
    data = f.read().split("\n")

heightmap = []
for line in data:
    row = [int(digit) for digit in line]
    heightmap.append(row)

result = 0
basins = []

for row in range(0, len(heightmap)):
    for position in range(0, len(heightmap[row])):
        neighbour = 0
        higher = 0
        current = heightmap[row][position]
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = row + direction[0], position + direction[1]
            if 0 <= x < len(heightmap) and 0 <= y < len(heightmap[row]):
                cur_ne = heightmap[x][y]
                neighbour += 1
                if heightmap[x][y] > heightmap[row][position]:
                    higher += 1
        if higher == neighbour and higher != 0:
            result += heightmap[row][position] + 1
            basins.append([row, position])

print("Part One: ", result)

all_basin_sizes = []
for i in basins:
    tiny_basin = [i]
    for number in tiny_basin:
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = number[0] + direction[0], number[1] + direction[1]
            if 0 <= x < len(heightmap) and 0 <= y < len(heightmap[number[0]]):
                if heightmap[x][y] != 9:
                    if [x, y] not in tiny_basin:
                        tiny_basin.append([x, y])
    all_basin_sizes.append(len(tiny_basin))

print("Part Two: ", sorted(all_basin_sizes)[-1] * sorted(all_basin_sizes)[-2] * sorted(all_basin_sizes)[-3])