#--- Day 10: Cathode-Ray Tube ---
with open('input.txt') as f:
    move = f.read().strip().split("\n")

def check(cycle, result):
    if cycle in cycles:
        result[:] = [result[0] + (cycle * x)]
        return result

def draw(crt):
    if cycle in crt_lines:
        print(crt)
        crt[:] = []
    elif len(crt) == x-1 or len(crt) == x or len(crt) == x+1:
        crt.append('#')
    else:
        crt.append(' ')
    return crt

x = 1; cycle = 0; result = [0]; cycles = [20, 60, 100, 140, 180, 220, 280]
crt_lines = [40, 80, 120, 160, 200, 240]; crt = []

for i in move:
    add = 0
    if i[0] == 'a':
        add = int(i[5:])
        cycle += 1
        draw(crt), check(cycle, result)
        cycle += 1
        draw(crt), check(cycle, result)
    else:
        cycle += 1
        draw(crt), check(cycle, result)
    x += add

print('Part One: ', result[0])
