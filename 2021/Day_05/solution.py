# --- Day 5: Hydrothermal Venture ---

def find_pairs(start_pair, end_pair, part):
    x1, y1 = start_pair
    x2, y2 = end_pair

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:
        return [(x1, y1 + i) for i in range(dy + 1)]
    elif dy == 0:
        return [(x1 + i, y1) for i in range(dx + 1)]
    else:
        if part == 1:
            return []
        else:
            return [(x1 + i, y1 + i) for i in range(abs(dx) + 1)]


def solution(part):
    parsed_input = []
    overlap = []

    with open('input.txt') as f:
        data = f.read().split("\n")

    for input_string in data:
        pair_strings = input_string.split(' -> ')
        parsed_pairs = [list(map(int, pair.split(','))) for pair in pair_strings]
        parsed_pairs.sort()
        all_pairs = find_pairs(parsed_pairs[0], parsed_pairs[1], part)
        for pair in all_pairs:
            if pair not in parsed_input:
                parsed_input.append(pair)
            elif pair not in overlap:
                overlap.append(pair)
    return len(overlap)


print("Part One: ", solution(1))
print("Part Two: ", solution(2))
