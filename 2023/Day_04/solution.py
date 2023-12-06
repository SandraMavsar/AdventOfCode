import re

def part_one():
    result = 0
    for line in lines:
        current_result = 0
        numbers = list(map(int, re.findall(r"\d+", line)))
        for number in numbers[1:11]:
            if number in numbers[11:]:
                if current_result == 0:
                    current_result = 1
                else: current_result *= 2
        result += current_result
    return result

def part_two():
    result = 0
    all_cards = {}
    for line in range(1, len(lines)+1):
        all_cards[line] = 1

    for line in lines:
        matching_cards = 0
        numbers = list(map(int, re.findall(r"\d+", line)))

        for number in numbers[1:11]:
            if number in numbers[11:]:
                matching_cards += 1

        for i in range(0, all_cards[numbers[0]]):
            for matches in range(1, matching_cards + 1):
                all_cards[matches+numbers[0]] += 1

    for key in all_cards:
        result += all_cards[key]
    return result


with open('input.txt') as f:
    lines = f.read().strip().split("\n")

print("Part One: ", part_one())
print("Part Two: ", part_two())