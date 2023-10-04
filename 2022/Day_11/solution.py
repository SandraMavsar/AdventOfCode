#--- Day 11: Monkey in the Middle ---

def solution(part):
    with open('input.txt', 'r') as f:
        current_monkey_name = None
        monkeys = {}
        inspection = {}
        product = 1  # product of all the "Divisible by xx" numbers, for part 2

        for line in f:
            line = line.strip()
            if line == "":
                current_monkey_name = None
            if "Monkey" in line and current_monkey_name is None:
                current_monkey_name = int(line.split()[1].rstrip(':'))
                monkeys[current_monkey_name] = {}
                inspection[current_monkey_name] = 0
            if current_monkey_name is not None:
                if "Starting" in line:
                    monkeys[current_monkey_name]["starting"] = [int(num) for num in line.split(":")[1].strip().split(', ')]
                if "Operation" in line:
                    operation = line.split(":")[1]
                    operation = operation.split(" ")[3:]
                    monkeys[current_monkey_name]["operation"] = operation
                if "Test" in line:
                    number = int(line.split(" ")[-1])
                    monkeys[current_monkey_name]["test"] = number
                    product *= number
                if "true" in line:
                    monkeys[current_monkey_name]["true"] = int(line.split(" ")[-1])
                if "false" in line:
                    monkeys[current_monkey_name]["false"] = int(line.split(" ")[-1])

        def new_worry_final(item1, item2, symbol):
            operations = {
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y
            }
            return operations[symbol](item1, item2)

        def new_worry(old, operation):
            return new_worry_final(old, old, operation[1])if operation[0] == "old" and operation[2] == "old" else \
                new_worry_final(old, int(operation[2]), operation[1])

        for cycle in range(0, part):
            for round in range(0, len(monkeys)):
                monkey = monkeys[round]
                for item in monkey["starting"]:
                    inspection[round] += 1
                    new_worry_lv = new_worry(item, monkey["operation"])
                    new_worry_lv = new_worry_lv // 3 if part == 20 else new_worry_lv % product
                    next_monkey = monkey["true" if new_worry_lv % monkey["test"] == 0 else "false"]
                    monkeys[next_monkey]["starting"].append(new_worry_lv)
                monkey["starting"] = []

        sorted_items = sorted(inspection.items(), key=lambda x: x[1])
        return sorted_items[-1][1] * sorted_items[-2][1]


print("Part One Solution: ", solution(20))
print("Part Two Solution: ", solution(10000))  # Chinese Remainder Theorem
