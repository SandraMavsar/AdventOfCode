# --- Day 1: Trebuchet?! ---

import re

def find_number(input_number):
    # Dictionary to pair strings to numbers
    word_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                 'nine': '9'}
    if input_number in word_dict.keys():
        real_number = word_dict.get(input_number)
        return real_number
    else:
        return str(input_number)

part_one = 0
part_two = 0

with open("input.txt", 'r') as f:
    for line in f:
        digits = re.findall(r'\d', line)
        if len(digits) == 1:
            result = int(str(digits[0]) + str(digits[0]))
            part_one += result
        else:
            result = int(str(digits[0]) + str(digits[-1]))
            part_one += result

        elements = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
        for item in elements:
            # Addresses strings tied together
            num = find_number(item)
            new_sub = item[0] + num + item[-1]
            line = re.sub(item, new_sub, line)
        elements = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
        if len(elements) == 1:
            number = find_number(elements[0])
            result = int(number + number)
            part_two += result
        else:
            front = find_number(elements[0])
            back = find_number(elements[-1])
            result = int(front + back)
            part_two += result

print("Part One: ", part_one)
print("Part Two: ", part_two)
