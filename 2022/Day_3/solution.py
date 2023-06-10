#--- Day 4: Camp Cleanup ---
import string

with open('input.txt') as f:
    input = [line.strip() for line in f.readlines()]

def part_one(alphabet):
    result = 0
    for line in input:
        for i in line[0: int(len(line) / 2)]:
            if i in line[(int((len(line) / 2))):]:
                result += alphabet.index(i) + 1
                break
    return result

def part_two(alphabet):
    result = 0; position = 0
    while position <= len(input)-3:
        slice = input[position:position + 3]
        for i in slice[0]:
            if i in slice[1] and i in slice[2]:
                result += alphabet.index(i) + 1
                break
        position += 3
    return result

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
print('Part One: ', part_one(alphabet))
print('Part Two ', part_two(alphabet))