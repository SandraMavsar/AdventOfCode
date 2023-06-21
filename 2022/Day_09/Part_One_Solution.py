#--- Day 9: Rope Bridge ---

with open('input.txt') as f:
    move = f.read().strip().split("\n")

    def move_tail(current_tail, current_head, previous_head):
        check = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if current_head == [current_tail[0]+i, current_tail[1]+j]:
                    check += 1
                    continue
        if check != 1:
            current_tail[:] = previous_head
            if previous_head not in tail:
                tail.append(previous_head)
        return current_tail

    current_head = [0,0]; previous_head = [0,0]; tail = [[0,0]]; current_tail = [0,0]
    moves = {'R': (1, 0), 'L': (-1, 0), 'D': (0, -1), 'U': (0, 1)}
    for i in move:
        for j in range(1, int(i[2:]) + 1):
            previous_head = current_head
            current_head = [current_head[0] + moves[i[0]][0], current_head[1] + moves[i[0]][1]]
            move_tail(current_tail, current_head, previous_head)

    print('Part One: ', len(tail))
