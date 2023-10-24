# --- Day 4: Giant Squid ---

def part_one():
    zeros = [0] * len(data[0])
    ones = [0] * len(data[0])
    for number in data:
        for i in range(0, len(number)):
            if number[i] == "0":
                zeros[i] += 1
            else:
                ones[i] += 1

    binary_number1 = ""
    binary_number2 = ""

    for i in range(0, len(zeros)):
        if zeros[i] > ones[i]:
            binary_number1 += "0"
            binary_number2 += "1"
        else:
            binary_number1 += "1"
            binary_number2 += "0"

    gama = int(binary_number1, 2)
    epsilon = int(binary_number2, 2)

    return gama * epsilon

def part_two(value):
    values = value.copy()
    ones = []
    zeros = []
    for bit_position in range(0, len(values[0])):
        for number in values:
            if number[bit_position] == "1":
                ones.append(number)
            else:
                zeros.append(number)
        if len(ones) >= len(zeros):
            values = ones.copy()
            ones = []
            zeros = []
        else:
            values = zeros.copy()
            ones = []
            zeros = []
        if len(values) == 1:
            return int(values[0], 2)


with open('input.txt') as f:
    data = f.read().split("\n")

print("Part One: ", part_one())
oxygen_generator_rating = part_two(data)
reverse_data = []
for number in data:
    current = ""
    for bit in number:
        if bit == "1":
            current += "0"
        else:
            current += "1"
    reverse_data.append(current)

co2_scrubber_rating = part_two(reverse_data)
print("Part Two: ", oxygen_generator_rating * co2_scrubber_rating)
