# --- Day 4: Giant Squid ---

import re

with open('input.txt') as f:
    data = f.read().split("\n")

number_draw = [int(num) for num in data[0].split(',')]
filtered_data = [item for item in data if item != ''][1:]

n = int(len(filtered_data) / 5)
boards = [[] for _ in range(n)]

board = 0
count = 0
for row in filtered_data:
    numbers = [int(match) for match in re.findall(r'\d+', row)]
    if count < 5:
        boards[board].append(numbers)
        count += 1
    else:
        board += 1
        boards[board].append(numbers)
        count = 1

marked_boards = boards.copy()
winnings = []


def calculate_result(board):
    remaining_num = 0
    for row in board:
        for number in row:
            if isinstance(number, int):
                remaining_num += number
    return remaining_num


def check_winner(board, total_winners, bingo_card):
    for row in board:
        if row.count("X") == 5:
            if bingo_card not in winnings:
                winnings.append(bingo_card)
            if len(winnings) == total_winners:
                return calculate_result(board)

    num_columns = len(board[0])
    for col in range(num_columns):
        column = [row[col] for row in board]
        if column.count("X") == 5:
            if bingo_card not in winnings:
                winnings.append(bingo_card)
            if len(winnings) == total_winners:
                return calculate_result(board)
    return 0


def start_bingo(total_winners):
    for draw in number_draw:
        for board in range(0, len(boards)):
            for row in range(0, len(boards[board])):
                if draw in boards[board][row]:
                    index = boards[board][row].index(draw)
                    marked_boards[board][row][index] = "X"
                    win = check_winner(marked_boards[board], total_winners, board)
                    if win != 0:
                        return win * draw


print("Part One: ", start_bingo(1))
print("Part Two: ", start_bingo(len(boards)))
