# map lists
a = []
b = []
c = []
d = []
e = []
f = []
g = []

maps = [a, b, c, d, e, f, g]

with open('input.txt', 'r') as x:
    for y in x.readlines():
        if not y.strip():
            continue
        if y.startswith('seeds:'):
            w = [int(z) for z in y.split()[1:]]
            continue
        elif y.startswith('seed-to-soil'):
            m = a
            continue
        elif y.startswith('soil-to-fertilizer'):
            m = b
            continue
        elif y.startswith('fertilizer-to-water'):
            m = c
            continue
        elif y.startswith('water-to-light'):
            m = d
            continue
        elif y.startswith('light-to-temperature'):
            m = e
            continue
        elif y.startswith('temperature-to-humidity'):
            m = f
            continue
        elif y.startswith('humidity-to-location'):
            m = g
            continue
        t = [int(z) for z in y.split()]
        m.append((t[1], t[2], t[0]))


def g(src, m):
    for s, r, d in m:
        if s <= src < s+r:
            return src - s + d
    return src


def g_loc(seed):
    t = seed
    for m in maps:
        t = g(t, m)
    return t

# part 1
print("Part One: ", min(g_loc(seed) for seed in w))

w_r = []
for i in range(0, len(w), 2):
    w_r.append((w[i], w[i]+w[i+1]-1))


def g_r(src_ranges, m):
    result = []
    for a, b in src_ranges:
        covered_ranges = []
        for s, r, d in m:
            x, y = s, s+r-1
            if b < x or y < a:
                continue
            inter1 = max(a, x)
            inter2 = min(b, y)
            covered_ranges.append((inter1, inter2))
            result.append((inter1-s+d, inter2-s+d))
        if not covered_ranges:
            result.append((a, b))
            continue
        covered_ranges.sort()
        if covered_ranges[0][0] > a:
            result.append((a, covered_ranges[0][0]-1))
        if covered_ranges[-1][1] < b:
            result.append((covered_ranges[-1][1]+1, b))
        for i in range(len(covered_ranges)-1):
            x1, y1 = covered_ranges[i]
            x2, y2 = covered_ranges[i+1]
            if x2 > y1+1:
                result.append((y1+1, x2-1))
    return result

t = w_r
for m in maps:
    t = g_r(t, m)
loc = t
print("Part Two: ", min(loc)[0])
