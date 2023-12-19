# --- Day 15: Lens Library ---
<<<<<<< Updated upstream
=======

def part_one(lines):
    result = 0
    for steps in lines:
        value = 0
        for character in steps:
            value += ord(character)
            value *= 17
            value %= 256
        result += value
    return result
>>>>>>> Stashed changes


with open('input.txt') as f:
    lines = f.read().strip().split(',')

    print("Part One: ", part_one(lines))


