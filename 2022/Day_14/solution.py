#--- Day 14: Regolith Reservoir ---
with open('input.txt') as f:
    data = f.read().strip().split('\n')

rocks = []
max_y = 0
for i in data:
    row = []
    a = i.split(' -> ')
    for j in a:
        x, y = j.split(',')
        row.append([int(x), int(y)])
        max_y = max(int(y), max_y)
    for k in range(0, len(row)-1):
        rocks.append(row[k])
        if row[k][0] == row[k+1][0]:
            steps = row[k+1][1] - row[k][1]
            if steps > 1:
                for l in range(1, steps):
                    rocks.append([row[k][0], row[k][1]+l])
            else:
                steps *= -1
                for l in range(1, steps):
                    rocks.append([row[k][0], row[k][1]-l])
        if row[k][1] == row[k+1][1]:
            steps = row[k][0] - row[k+1][0]
            if steps > 1:
                for l in range(1, steps):
                    rocks.append([row[k][0]-l, row[k][1]])
            else:
                steps *= -1
                for l in range(1, steps):
                    rocks.append([row[k][0] + l, row[k][1]])

    rocks.append(row[-1])

sand = [[500,0]]
floor = max_y + 2
for i in range(sand[0][0] - (floor + 10), sand[0][0] + (floor + 10)):
    rocks.append([i, floor])

falling = True
part_one = 0

while falling == True:
    falling_sand = True
    current_falling_pos = sand[0]
    while falling_sand == True:
        if [499, 1] in rocks and [500, 1] in rocks and [501, 1] in rocks:
            falling = False
            print('Part Two: ', len(sand))
            break
        if current_falling_pos[1] > max_y and part_one == 0:
            print('Part One: ', len(sand)-1)
            part_one = 1
        if [current_falling_pos[0], current_falling_pos[1]+1] not in rocks:
            a = [current_falling_pos[0], current_falling_pos[1]+1]
            current_falling_pos = [current_falling_pos[0], current_falling_pos[1] + 1]
            continue
        if [current_falling_pos[0]-1, current_falling_pos[1]+1] not in rocks:
            a = [current_falling_pos[0]-1, current_falling_pos[1]+1]
            current_falling_pos = [current_falling_pos[0] - 1, current_falling_pos[1] + 1]
            continue
        if [current_falling_pos[0]+1, current_falling_pos[1]+1] not in rocks:
            a = [current_falling_pos[0]+1, current_falling_pos[1]+1]
            current_falling_pos = [current_falling_pos[0] + 1, current_falling_pos[1] + 1]
            continue
        else:
            sand.append(current_falling_pos)
            rocks.append(current_falling_pos)
            falling_sand = False
