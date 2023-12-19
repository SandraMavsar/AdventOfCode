# --- Day 18: Lavaduct Lagoon ---

def part_one(lines):
    decoded_instructions = []
    for line in lines:
        d, n, _ = line
        instruction_tuple = (d, int(n))
        decoded_instructions.append(instruction_tuple)

    return decoded_instructions


def part_two(lines):
    decoded_instructions = []
    for line in lines:
        color = line[2]
        direction = "RDLU"[int(color[7])]
        distance = int(color[2:7], 16)
        instruction_tuple = (direction, distance)
        decoded_instructions.append(instruction_tuple)

    return decoded_instructions


def find_area(instructions):
    total_perimeter, total_shoelace = 0, 0
    current_x, current_y, points = 0, 0, [(0, 0)]

    for direction, distance in instructions:
        delta_x, delta_y = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}[direction]
        current_x, current_y = current_x + delta_x * distance, current_y + delta_y * distance
        points.append((current_x, current_y))
        total_perimeter += distance

    # Calculate the shoelace formula for the points to determine the area
    shoelace = sum((a[0] * b[1] - b[0] * a[1]) for a, b in zip(points, points[1:])) // 2

    # Calculate the total area by adding shoelace, half of the perimeter, and 1
    total_area = shoelace + total_perimeter // 2 + 1
    return total_area


with open('input.txt') as f:
    input_data = f.read()

lines = [line.split() for line in input_data.splitlines()]

print("Part One: ", find_area(part_one(lines)))
print("Part Two: ", find_area(part_two(lines)))