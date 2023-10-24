# --- Day 7: The Treachery of Whales ---

def part_one():
    min_sum_of_differences = float('inf')
    for num in crabs:
        sum_of_differences = sum(abs(num - other) for other in crabs)

        if sum_of_differences < min_sum_of_differences:
            min_sum_of_differences = sum_of_differences

    return min_sum_of_differences


def part_two():
    min_fuel = float('inf')
    crabs.sort()
    for number in range(crabs[0], crabs[-1]+1):
        total_fuel = 0
        for crab in crabs:
            steps = abs(crab - number)
            for i in range(1, steps+1):
                total_fuel += i
        if min_fuel > total_fuel:
            min_fuel = total_fuel

    return min_fuel


with open('input.txt') as f:
    data = f.read().split("\n")
    crabs = [int(num) for num in data[0].split(',')]

    print("Part One: ", part_one())
    print("Part Two: ", part_two())
