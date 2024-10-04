# --- Day 11: Cosmic Expansion ---

def calculate_distance(factor):
    distance = 0
    for galaxy in range(0, len(galaxies)):
        for other_galaxy in galaxies[galaxy+1:]:
            distance += (other_galaxy[0] - galaxies[galaxy][0] + abs(galaxies[galaxy][1] - other_galaxy[1]))
            for row in rows_to_multiply:
                if galaxies[galaxy][0] < row < other_galaxy[0]:
                    distance += factor
            for col in cols_to_multiply:
                if min(galaxies[galaxy][1], other_galaxy[1]) < col < max(other_galaxy[1], galaxies[galaxy][1]):
                    distance += factor

    return distance

with open('input.txt') as f:
    lines = f.read().strip().split('\n')

    rows_to_multiply = [i for i, line in enumerate(lines) if '#' not in line]
    cols_to_multiply = [j for j in range(len(lines[0])) if all(line[j] == '.' for line in lines)]

    galaxies = []
    for row in range(0, len(lines)):
        for character in range(0, len(lines[row])):
            if lines[row][character] == "#":
                galaxies.append([row, character])

print('Part One: ', calculate_distance(1))
print('Part Two: ', calculate_distance(999999))



