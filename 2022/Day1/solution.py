#--- Day 1: Calorie Counting ---
input = []
with open('input.txt') as f:
    [input.append(line.strip()) for line in f.readlines()]

most_cal = []; current = 0
for i in input:
    if i == '':
        most_cal.append(current)
        current = 0
    else:
        current += int(i)
most_cal.append(current)
most_cal.sort(reverse = True)

print('Part One: ', most_cal[0])
print('Part Two: ', sum(most_cal[0:3]))