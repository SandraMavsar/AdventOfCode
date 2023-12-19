# --- Day 15: Lens Library ---


with open('input.txt') as f:
    lines = f.read().strip().split('\n')

    map_rows = [list(line) for line in lines]
    map_columns = list(zip(*map_rows))

    for i in range(0, 100):
        def move_zeros_left(column):
            moved_column = list(column)
            for i in range(len(moved_column)):
                if moved_column[i] == 'O':
                    for j in range(i - 1, -1, -1):
                        if moved_column[j] == '#':
                            break
                        if moved_column[j] == '.':
                            moved_column[j], moved_column[j + 1] = moved_column[j + 1], moved_column[j]
            return tuple(moved_column)

        map_columns_north = [move_zeros_left(column) for column in map_columns]

    result = 0
    for column in map_columns_north:
        for index, character in enumerate(column):
            if character == "O":
                result += len(column) - index

    print("Part One: ", result)





