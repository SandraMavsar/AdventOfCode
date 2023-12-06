# --- Day 3: Gear Ratios ---

def part_one(current_positions):
    rows, cols = len(engine), len(engine[0])
    for coordinates in current_positions:
        i, j = coordinates[0], coordinates[1]
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
            x, y = i + direction[0], j + direction[1]
            if 0 <= x < rows and 0 <= y < cols:
                if engine[x][y] in symbols:
                    return True
    return False

with open('input.txt') as f:
    input = f.read()
    engine = [list(line.strip()) for line in input.strip().split('\n')]
    symbols = "!@#$%^&*()_+-=\][{}|:;/?<>"
    solution = 0
    rows, cols = len(engine), len(engine[0])
    part_number_sum = 0
    current_number = ''
    current_positions = []
    for i in range(rows):
        if len(current_number) > 0:
            if part_one(current_positions):
                solution += int(current_number)
        current_number = ''
        current_positions = []
        for j in range(cols):
            if engine[i][j] not in symbols and engine[i][j] != '.':
                current_number += engine[i][j]
                current_positions.append((i, j))
            else:
                if len(current_number) > 0:
                    if part_one(current_positions):
                        solution += int(current_number)
                    current_number = ''
                    current_positions = []

print("Part One: ", solution)




