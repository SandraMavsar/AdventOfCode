#--- Day 12: Hill Climbing Algorithm ---

from collections import deque

def is_valid_movement(elevation1, elevation2):
    if elevation1 == "S":
        return True
    if elevation2 == "E":
        return ord("z") - ord(elevation1) <= 1
    return ord(elevation2) - ord(elevation1) <= 1

def create_graph(heightmap):
    graph = {}
    rows, cols = len(heightmap), len(heightmap[0])

    for i in range(rows):
        for j in range(cols):
            node = (i, j)
            graph[node] = []

            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = i + direction[0], j + direction[1]

                # Check grid boundaries
                if 0 <= x < rows and 0 <= y < cols:
                    if is_valid_movement(heightmap[i][j], heightmap[x][y]):
                        if (x, y) != (0, 0):
                            graph[node].append((x, y))

    return graph

def bfs_shortest_steps(graph, start, end):
    queue = deque([(start, 0)])  
    visited = set()

    while queue:
        current_node, steps = queue.popleft()

        if current_node == end:
            return steps

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor in graph[current_node]:
            queue.append((neighbor, steps + 1))

    return float('inf')

with open('inputTest.txt') as f:
    input = f.read()

    grid = [list(line.strip()) for line in input.strip().split('\n')]
    start_pos = None
    start_pos_part2 = []
    end_pos = None

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start_pos = (i, j)
            if grid[i][j] == 'a' or grid[i][j] == "S":
                start_pos_part2.append((i, j))
            elif grid[i][j] == 'E':
                end_pos = (i, j)

    graph = create_graph(grid)
    solutions = []

    for i in start_pos_part2:
        solutions.append(bfs_shortest_steps(graph, i, end_pos))

    print("Part One: ", bfs_shortest_steps(graph, start_pos, end_pos))
    print("Part Two: ", sorted(solutions)[0])
