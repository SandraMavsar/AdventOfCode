import re

with open('input.txt') as f:
    result1 = 0; result2 = 0
    lines = f.read().strip().split("\n")
    for line in lines:
        numbers = list(map(int, re.findall(r"\d+", line)))
        if (numbers[0] == sorted(numbers)[0] and numbers[1] == sorted(numbers)[-1]) or \
            (numbers[2] == sorted(numbers)[0] and numbers[3] == sorted(numbers)[-1]):
            result1 += 1
        if (numbers[0] >= numbers[2] and numbers[0] <= numbers[3]) or \
            (numbers[1] >= numbers[2] and numbers[1] <= numbers[3]) or \
            (numbers[2] >= numbers[0] and numbers[2] <= numbers[1]) or \
            (numbers[3] >= numbers[0] and numbers[3] <= numbers[1]):
            result2 += 1

    print('Part One: ', result1)
    print('Part Two: ', result2)
