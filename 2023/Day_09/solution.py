# --- Day 9: Mirage Maintenance ---

from math import comb
# Pascal's triangle
# Calculate the binomial coefficient "n choose k"
# n is the total number of items.
# k is the number of items to choose.
# result = comb(n, k)
# The function returns the number of ways to choose k items from a set of n items, without regard to the order of selection.

with open("input.txt", "r") as file:
    lines = file.readlines()
    part_one = 0
    part_two = 0
    for line in lines:
        formatted_line = line.split()

        for index, value in enumerate(formatted_line):
            # Calculate the binomial coefficient (n choose k) using the comb function from the math module
            pascal = comb(len(formatted_line), index)

            # Update the part_one using the formula provided
            # value * binomial_coefficient * (-1)^(n - k + 1)
            part_one += int(value) * pascal * (-1) ** (len(formatted_line) - index + 1)

        reverse_formatted_line = line.split()
        reverse_formatted_line = reverse_formatted_line[::-1]
        for index, value in enumerate(reverse_formatted_line):

            pascal = comb(len(reverse_formatted_line), index)
            part_two += int(value) * pascal * (-1) ** (len(reverse_formatted_line) - index + 1)

print("Part One: ", part_one)
print("Part Two: ", part_two)
