# --- Day 1: Sonar Sweep ---

def part_one(sonar_sweep):
    current = sonar_sweep[0]
    increase = 0
    for i in sonar_sweep[1:]:
        if current < i:
            increase += 1
        current = i
    return increase

def part_two(sonar_sweep):
    current = sum(sonar_sweep[:3])
    increase = 0
    for i in range(1, len(sonar_sweep)-2):
        if current < sum(sonar_sweep[i:i+3]):
            increase += 1
        current = sum(sonar_sweep[i:i+3])
    return increase

with open('input.txt') as f:
    data = f.read().split()
sonar_sweep = [int(item) for item in data]

print("Part One: ", part_one(sonar_sweep))
print("Part Two: ", part_two(sonar_sweep))