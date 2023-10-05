#--- Day 22: Monkey Map ---

with open('input.txt') as f:
    lines = f.readlines()

    first = None
    mat = []
    length = len(lines[0].replace('\n', ''))

    for j, line in enumerate(lines):
        if line == '\n':
            moves = lines[j + 1]
            break
        row = []
        line = line.ljust(length+1)
        for i, ch in enumerate(line):
            if ch != '\n':
                if ch == '.' and not first:
                    first = (i, j)
                row.append(ch)
        mat.append(''.join(row))

    direction = (1, 0)
    directions = {
        (1, 0): {'R': (0, 1), 'L': (0, -1)},
        (0, 1): {'R': (-1, 0), 'L': (1, 0)},
        (-1, 0): {'R': (0, -1), 'L': (0, 1)},
        (0, -1): {'R': (1, 0), 'L': (-1, 0)},
    }

    def start_moving(point, direction, step):
        x, y = point
        dx, dy = direction
        pos = (x, y)
        while step > 0:
            x += dx
            y += dy
            if x == len(mat[0]):
                x = 0
            elif x < 0:
                x = len(mat[0]) - 1
            elif y == len(mat):
                y = 0
            elif y < 0:
                y = len(mat) - 1
            if mat[y][x] == '#':
                return pos
            if mat[y][x] == ' ':
                continue
            step -= 1
            pos = (x, y)
        return x, y

    s = ''
    facing = first
    for move in moves + 'L':
        if move in 'RL':
            step = int(s)
            lastDir = direction
            facing = start_moving(facing, direction, step)
            s = ''
            direction = directions[direction][move]
        else:
            s += move

    print('Part One: ', (facing[0] + 1) * 4 + (facing[1] + 1) * 1000 + list(directions).index(lastDir))
