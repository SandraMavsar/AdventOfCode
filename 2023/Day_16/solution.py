# --- Day 16: The Floor Will Be Lava ---

def part_one():
    grid = []
    lines = data.split("\n")
    for line in lines:
        grid.append(list(line))

    beams = [(0, 0, 1, 0)]
    seen_positions = set()
    energized_positions = set()

    while len(beams) > 0:
        new_beams = []

        for beam in beams:
            x, y, dx, dy = beam

            if (x, y, dx, dy) in seen_positions:
                continue

            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                continue

            seen_positions.add((x, y, dx, dy))
            energized_positions.add((x, y))

            if grid[y][x] == "/":
                if dx == 1 and dy == 0:
                    dx, dy = 0, -1
                elif dx == -1 and dy == 0:
                    dx, dy = 0, 1
                elif dx == 0 and dy == 1:
                    dx, dy = -1, 0
                else:
                    dx, dy = 1, 0
                new_beams.append((x + dx, y + dy, dx, dy))
            elif grid[y][x] == "\\":
                if dx == 1 and dy == 0:
                    dx, dy = 0, 1
                elif dx == -1 and dy == 0:
                    dx, dy = 0, -1
                elif dx == 0 and dy == 1:
                    dx, dy = 1, 0
                else:
                    dx, dy = -1, 0
                new_beams.append((x + dx, y + dy, dx, dy))
            elif dy == 0 and grid[y][x] == "|":
                new_beams.append((x, y, 0, -1))
                new_beams.append((x, y, 0, 1))
            elif dx == 0 and grid[y][x] == "-":
                new_beams.append((x, y, -1, 0))
                new_beams.append((x, y, 1, 0))
            else:
                new_beams.append((x + dx, y + dy, dx, dy))
        beams = new_beams
    return len(energized_positions)

def count_energized(grid, initial_beam):
    grid_width = len(grid[0])
    grid_height = len(grid)

    beams = [initial_beam]
    seen_positions = set()
    energized_positions = set()

    while beams:
        new_beams = []

        for beam in beams:
            x, y, dx, dy = beam

            if (x, y, dx, dy) in seen_positions:
                continue

            if x < 0 or x >= grid_width or y < 0 or y >= grid_height:
                continue

            seen_positions.add((x, y, dx, dy))
            energized_positions.add((x, y))

            if grid[y][x] == "/":
                if dx == 1 and dy == 0:
                    dx, dy = 0, -1
                elif dx == -1 and dy == 0:
                    dx, dy = 0, 1
                elif dx == 0 and dy == 1:
                    dx, dy = -1, 0
                else:
                    dx, dy = 1, 0

                new_beams.append((x + dx, y + dy, dx, dy))
            elif grid[y][x] == "\\":
                if dx == 1 and dy == 0:
                    dx, dy = 0, 1
                elif dx == -1 and dy == 0:
                    dx, dy = 0, -1
                elif dx == 0 and dy == 1:
                    dx, dy = 1, 0
                else:
                    dx, dy = -1, 0

                new_beams.append((x + dx, y + dy, dx, dy))
            elif dy == 0 and grid[y][x] == "|":
                new_beams.append((x, y, 0, -1))
                new_beams.append((x, y, 0, 1))
            elif dx == 0 and grid[y][x] == "-":
                new_beams.append((x, y, -1, 0))
                new_beams.append((x, y, 1, 0))
            else:
                new_beams.append((x + dx, y + dy, dx, dy))

        beams = new_beams

    return len(energized_positions)

def part_two():

    lines = data.split("\n")
    grid = []
    for line in lines:
        grid.append(list(line))

    grid_width = len(grid[0])
    grid_height = len(grid)

    max_energized = 0

    for x in range(grid_width):
        max_energized = max(max_energized, count_energized(grid, (x, 0, 0, 1)))
        max_energized = max(max_energized, count_energized(grid, (x, grid_height - 1, 0, -1)))

    for y in range(grid_height):
        max_energized = max(max_energized, count_energized(grid, (0, y, 1, 0)))
        max_energized = max(max_energized, count_energized(grid, (grid_width - 1, y, -1, 0)))

    return max_energized

with open('input.txt') as f:
    data = f.read().strip()

print("Part One: ", part_one())
print("Part Two: ", part_two())
