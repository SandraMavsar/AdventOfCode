# --- Day 6: Lanternfish ---

with open('input.txt') as f:
    data = f.read().split("\n")
fishes = [int(num) for num in data[0].split(',')]

for day in range(0, 256):
    current = []
    new_fish = 0
    for fish in fishes:
        if fish == 0:
            current.append(6)
            new_fish += 1
        else:
            current.append(fish-1)
    new_fish_list = [8 for _ in range(new_fish)]
    fishes = current + new_fish_list
    if day == 79:
        print("Part One: ", len(fishes))

print("Part Two: ", len(fishes))
