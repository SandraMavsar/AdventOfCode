# --- Day 15: Chiton ---

with open('input.txt') as f:
    data = f.read().split("\n")
    map = [list(map(int, element)) for element in data]
    print(map)
