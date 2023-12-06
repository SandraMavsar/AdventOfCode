# --- Day 1: Trebuchet?! ---

def part_one():
    total_sum_part1 = 0
    for line in data:
        digits_only = [char for char in line if char.isdigit()]
        current = digits_only[0] + digits_only[-1]
        total_sum_part1 += int(current)
    return total_sum_part1


def part_two():
    total_sum_part2 = 0
    for line in data:
        line = line.strip("\n")
        current = ''
        print(line)
        digits_only = [char for char in line if char.isdigit()]
        substring = ["nine", "eight", "seven", "one", "two", "three", "four", "five", "six", "eight", ]
        values = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        index_one = line.index(digits_only[0])
        index_two = line.index(digits_only[-1])
        for length in range(0, index_one + 1):
            if current == '':
                for subs in substring:
                    if subs in line[0:length]:
                        current = str(values[subs])
        line = current + line
        index_two += 1
        current = ''
        backward = ''
        if current == '':
            for char in line[::-1]:
                backward = char + backward
                if len(line) - len(backward) == index_two:
                    break
                else:
                    for subs in substring:
                        if subs in backward:
                            current = str(values[subs])
                            break
        line = line + current
        print("end", line)

    return total_sum_part2

with open('input.txt') as f:
    with open('input.txt') as f:
        data = f.readlines()

#print("Part One: ", part_one())
print("Part Two: ", part_two())
