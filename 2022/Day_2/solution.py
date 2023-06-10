#--- Day 2: Rock Paper Scissors ---
input = []
with open('input.txt') as f:
    [input.append(line.strip()) for line in f.readlines()]

def first_part():
    points = {'X': 1, 'Y': 2, 'Z': 3}
    combos = {'A': (('X', 3), ('Y', 6), ('Z', 0)), 'B': (('X', 0), ('Y', 3), ('Z', 6)),
              'C': (('X', 6), ('Y', 0), ('Z', 3))}

    result = 0
    for i in input:
        for j in combos[i[0]]:
            if i[2] in j:
                result = result + j[1] + points[i[2]]
    return result

def second_part():
    points = {'X': 0, 'Y': 3, 'Z': 6}
    combos = {3: (('A', 1), ('B', 2), ('C', 3)), 0: (('A', 3), ('B', 1), ('C', 2)),
              6: (('A', 2), ('B', 3), ('C', 1))}

    result = 0
    for i in input:
        for j in combos[points[i[2]]]:
            if i[0] in j:
                result = result + j[1] + points[i[2]]

    return result

print('Part One: ', first_part())
print('Part Two: ', second_part())