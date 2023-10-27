# --- Day 11: Dumbo Octopus ---

with open('input.txt') as f:
    data = f.read().split("\n")
    octopuses = [list(map(int, element)) for element in data]

number_of_flashes = 0
steps = 0
while steps != -1:
    flashed = []
    afflicted = []

    def flashing(row, column):
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
            x, y = row + direction[0], column + direction[1]
            if 0 <= x < 10 and 0 <= y < 10:
                afflicted.append([x, y])

    def afflicted_octo():
        afflicted_copy = afflicted.copy()
        for flash in afflicted_copy:
            if flash not in flashed:
                octopuses[flash[0]][flash[1]] += 1
                if octopuses[flash[0]][flash[1]] > 9:
                    flashing(flash[0], flash[1])
                    flashed.append(([flash[0], flash[1]]))
                    octopuses[flash[0]][flash[1]] = 0
            afflicted.pop(0)
        if len(afflicted) != 0:
            afflicted_octo()

    for row in range(0, 10):
        for column in range(0, 10):
            octo1 = octopuses[row][column]
            octopuses[row][column] += 1
            octo = octopuses[row][column]
            if octopuses[row][column] > 9:
                flashed.append([row, column])
                octopuses[row][column] = 0
                flashing(row, column)
    afflicted_octo()

    if steps < 100:
        number_of_flashes += len(flashed)
    steps += 1

    if len(flashed) == 100:
        print("Part Two: ", steps)
        steps = -1

print("Part One: ", number_of_flashes)
