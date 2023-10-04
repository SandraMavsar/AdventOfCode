# --- Day 21: Monkey Math ---

operation = {}
result = {}

def contains_symbol(input_string):
    symbols = ['*', '-', '/', '+']
    return any(symbol in input_string for symbol in symbols)


with open('input.txt') as f:
    lines = f.read().strip().split("\n")
    for i in lines:
        a = i.split(":")
        if contains_symbol(a[1]):
            b = a[1].strip().split(" ")
            operation[a[0]] = b
        else:
            result[a[0]] = int(a[1].strip())

while("root" not in result):
   for key, value in operation.items():
       if value[0] in result and value[2] in result:
           if value[1] == "+":
               result[key] = result[value[0]] + result[value[2]]
           elif value[1] == "-":
               result[key] = result[value[0]] - result[value[2]]
           elif value[1] == "*":
               result[key] = result[value[0]] * result[value[2]]
           elif value[1] == "/":
               result[key] = result[value[0]] / result[value[2]]

print("Part One: ", result["root"])
