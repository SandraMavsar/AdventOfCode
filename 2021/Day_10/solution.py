# --- Day 10: Syntax Scoring ---

with open('input.txt') as f:
    data = f.read().split("\n")


def check_incomplete(stack):
    incomplete = {"(": 1, "[": 2, "{": 3, "<": 4}
    score = 0
    stack.reverse()
    for symbol in stack:
        score *= 5
        score += incomplete[symbol]

    return True, score


def check_symbol_order(symbols):
    stack = []

    open_symbols = "({[<"
    close_symbols = ")}]>"

    for symbol in symbols:
        if symbol in open_symbols:
            stack.append(symbol)
        elif symbol in close_symbols:
            index = close_symbols.index(symbol)
            if stack and stack[-1] == open_symbols[index]:
                stack.pop()
            else:
                return False, symbol

    if len(stack) == 0:
        return True, 0
    else:
        return check_incomplete(stack)


illegal = {")": 3, "]": 57, "}": 1197, ">": 25137}
incomplete_count = []
illegal_count = 0
for line in data:
    verified = check_symbol_order(line)
    if not verified[0]:
        illegal_count += illegal[verified[1]]
    else:
        if verified[1] != 0:
            incomplete_count.append(verified[1])

print("Part One: ", illegal_count)
print("Part Two: ", sorted(incomplete_count)[int(len(incomplete_count)/2)])