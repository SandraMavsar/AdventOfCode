# --- Day 6: Wait For It ---

def part_one():
    result = 1
    for race in results1:
        current_wins = 0
        duration, distance_to_beat = race[0], race[1]
        for seconds in range(0, duration):
            distance = seconds * (duration - seconds)
            if distance > distance_to_beat:
                current_wins += 1
        result *= current_wins
    return result

def part_two():
    current_wins = 0
    duration, distance_to_beat = results2[0], results2[1]
    for seconds in range(0, duration):
        distance = seconds * (duration - seconds)
        if distance > distance_to_beat:
            current_wins += 1
    return current_wins

# test_results1 = [[7, 9], [15, 40], [30, 200]]
# test_results2 = [71530, 940200]

results1 = [[44, 202], [82, 1076], [69, 1138], [81, 1458]]
results2 = [44826981, 202107611381458]

print('Part One: ', part_one())
print('Part Two: ', part_two())

