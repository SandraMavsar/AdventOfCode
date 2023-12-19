# --- Day 10: Pipe Maze ---

from collections import deque

def is_a_valid_graph(graph_to_check):
    valid_graph = {}
    for key in graph_to_check:
        nodes = []
        for node in graph_to_check[key]:
            if key in graph_to_check[node]:
                nodes.append(node)
        if len(nodes) > 0:
            valid_graph[key] = nodes
    return valid_graph

def create_graph(map):
    graph = {}
    rows, cols = len(map), len(map[0])

    for i in range(rows):
        for j in range(cols):
            node = (i, j)
            graph[node] = []
            for direction in movement[map[i][j]]:
                x, y = i + move[direction][0], j + move[direction][1]
                if 0 <= x < rows and 0 <= y < cols:
                    graph[node].append((x, y))

    return graph

def find_farthest_tile(graph, start):
    visited = set()
    queue = deque([(start, 0)])  # Using a queue to perform BFS

    farthest_tile = start
    max_distance = 0

    while queue:
        current, distance = queue.popleft()
        visited.add(current)

        if distance > max_distance:
            farthest_tile = current
            max_distance = distance

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

    return farthest_tile, max_distance, visited

def coordinates_to_edge(node, rows, cols, loop_line):
    x, y = node
    coordinates = [0, 0, 0, 0]

    for i in range(x - 1, -1, -1):
        if (i, y) in loop_line:
            coordinates[0] += 1
        if i == 0:
            break

    for i in range(x + 1, rows):
        if (i, y) in loop_line:
            coordinates[1] += 1
        if i == rows - 1:
            break

    for j in range(y - 1, -1, -1):
        if (x, j) in loop_line:
            coordinates[2] += 1
        if j == 0:
            break

    for j in range(y + 1, cols):
        if (x, j) in loop_line:
            coordinates[3] += 1
        if j == cols - 1:
            break

    crosses = 0
    for i in coordinates:
        if i % 2 != 0:
            crosses += 1

    if crosses == 4:
        return True
    else:
        return False

def enclosed_area(loop_line):
    rows, cols = len(pipes_map), len(pipes_map[0])
    enclosed = 0
    for i in range(rows):
        for j in range(cols):
            node = (i, j)
            if node not in loop_line:
                if coordinates_to_edge(node, rows, cols, loop_line):
                    enclosed += 1

    return enclosed


with open('input.txt') as f:
    lines = f.read().splitlines()
    pipes_map = []
    for line in lines:
        row = []
        for character in line:
            row.append(character)
        pipes_map.append(row)

    start_pos = None
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                start_pos = (i, j)

    movement = {"|": ["N", "S"], "-": ["E", "W"], "L": ["N", "E"], "J": ["N", "W"], "7": ["W", "S"], "F": ["E", "S"], ".": [], "S": ["N", "S", "E", "W"]}
    move = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
    graph = is_a_valid_graph(create_graph(pipes_map))
    solution_part1, loop_in_graph = find_farthest_tile(graph, start_pos)[1], find_farthest_tile(graph, start_pos)[2]

    print("Part One: ", solution_part1)
    print("Part Two: ", enclosed_area(loop_in_graph))
