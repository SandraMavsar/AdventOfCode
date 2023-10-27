# --- Day 14: Extended Polymerization ---

with open('input.txt') as f:
    data = f.read()

template, insertion_rules_all = data.split('\n\n', 1)
insertion_rules = insertion_rules_all.strip().split('\n')

pairs = {}
for i in insertion_rules:
    pair = i.split("->")
    clean_pair = [elem.strip() for elem in pair]
    pairs[clean_pair[0]] = clean_pair[1]


def polymer_growth(step, polymer, max_step):
    if step < max_step:
        new_polymer = ""
        for i in range(0, len(polymer) - 1):
            new_polymer += polymer[i] + pairs[polymer[i:i + 2]]
        new_polymer += polymer[-1]
        return polymer_growth(step + 1, new_polymer, max_step)
    else:
        values = []
        for i in template:
            values.append(polymer.count(i))
        values.sort()
        return values[-1]-values[0]


print("Part One: ", polymer_growth(0, template, 10))
print("Part Two: ", polymer_growth(0, template, 40))
