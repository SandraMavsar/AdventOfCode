#--- Day 8: Treetop Tree House ---

with open('input.txt') as f:
    trees = f.read().strip().split("\n")

visible = 2 * len(trees) + 2 * len(trees[0]) - 4
tree_house = []

def check_horizontal(row, column, tree_heigth):
    before = 0; after = 0
    possible = 0
    up = 0; down = 0

    for tree in range(row - 1, -1, -1):
        if int(trees[tree][column]) >= tree_heigth:
            up += 1
            break
        else:
            up += 1
            before += 1
    if before == row:
        possible += 1

    for tree in range(row + 1, len(trees[0])):
        if int(trees[tree][column]) >= tree_heigth:
            down += 1
            break
        else:
            down += 1
            after += 1
    if after == len(trees[0]) - row - 1 and possible == 0:
        possible += 1

    return [possible, up*down]

def check_vertical(row, column, tree_heigth):
    before = 0; after = 0
    possible = 0
    left = 0; right = 0

    for tree in range(column-1, -1, -1):
        if int(trees[row][tree]) >= tree_heigth:
            left += 1
            break
        else:
            left += 1
            before += 1
    if before == column:
        possible += 1

    for tree in range(column + 1, len(trees[row])):
        if int(trees[row][tree]) >= tree_heigth:
            right += 1
            break
        else:
            right += 1
            after += 1

    if after == len(trees[row]) - column - 1 and possible == 0:
        possible += 1

    return [possible, left * right]


for row in range(1, len(trees)-1):
    for column in range(1, len(trees[row])-1):
        vertical = check_vertical(row, column, int(trees[row][column]))
        horizontal = check_horizontal(row, column, int(trees[row][column]))
        tree_house.append(vertical[1]*horizontal[1])
        if vertical[0] == 1:
            visible += 1
        elif horizontal[0] == 1:
            visible += 1

print("Part One: ", visible)
print("Part Two: ", sorted(tree_house)[-1])
