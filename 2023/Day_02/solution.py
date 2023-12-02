#--- Day 2: Cube Conundrum ---
import re

with open('input.txt') as f:
    data = f.read().split('\n')

total_sum_part1 = 0
total_sum_part2 = 0

for i in data:
    words_to_extract = ["red", "blue", "green"]
    digits = re.findall(r"\d+", i)
    pattern = re.compile(r'\b(?:' + '|'.join(words_to_extract) + r')\b')
    extracted_words = pattern.findall(i)

    valid_digits = {'red': 12, 'green': 13, 'blue': 14}
    current_digits = {'red': 0, 'green': 0, 'blue': 0}

    colors = 0
    for position in range(0, len(extracted_words)):
        if int(digits[position + 1]) > current_digits[extracted_words[position]]:
            current_digits[extracted_words[position]] = int(digits[position + 1])
        if int(digits[position + 1]) <= valid_digits[extracted_words[position]]:
            colors += 1
    # part_one

    if colors == len(extracted_words):
        total_sum_part1 += int(digits[0])

    # part_two
    possible_game = 1
    for value in current_digits.values():
        possible_game *= int(value)
    total_sum_part2 += possible_game

print("part One: ", total_sum_part1)
print("part Two: ", total_sum_part2)
