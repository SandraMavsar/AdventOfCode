#--- Day 6: Tuning Trouble ---
with open('input.txt') as f:
    lines = f.readline().strip()

def solution(message):
    for i in range(0, len(lines)-(message - 1)):
        segment = lines[i: i+message]
        unique = 0
        for j in segment:
            if segment.count(j) == 1:
                unique += 1
            else:
                break
        if unique == message:
            return i+message
            break

print('Part One: ', solution(4))
print('Part Two: ', solution(14))