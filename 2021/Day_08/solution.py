# --- Day 8: Seven Segment Search ---

with open('input.txt') as f:
    data = f.read().split("\n")

final_result = []

for input_str in data:
    sections = input_str.split(', ')
    result = []
    for section in sections:
        subsections = section.split(' | ')
        words_lists = [sub.split() for sub in subsections]
        result.extend(words_lists)

    final_result.append(result)


def part_one():
    result = 0
    for i in final_result:
        for word in i[1]:
            if len(word) == 2 or len(word) == 3 or len(word) == 4 or len(word) == 7:
                result += 1
    return result


def part_two(result):
    patterns = {"acedgfb": 8, "cdfbe":5, "gcdfa":2, "fbcad":3, "dab":7, "cefabd":9, "cdfgeb":6, "eafb":4, "cagedb":0, "ab":1}
    for i in final_result:
        number = ""
        for word in i[1]:
            number += patterns[word]
        result += int(number)
    return result

result = 0
print("Part One: ", part_one())
print("Part Two: ", part_two(result))
