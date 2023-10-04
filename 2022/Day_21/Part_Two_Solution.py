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
            if a[0] == "root":
                to_check = [a[1].strip().split(" ")[0], a[1].strip().split(" ")[2]]
            else:
                b = a[1].strip().split(" ")
                operation[a[0]] = b
        else:
            if a[0] == 'humn':
                result[a[0]] = 0
            result[a[0]] = int(a[1].strip())

#print(operation)
print("Part Two: ", result)

y = 0
while y == 0:
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
       if to_check[0] in result and to_check[1] in result:
           if to_check[0] == to_check[1]:
               print(result["humn"])
               y = 1
       result["humn"] += 1
