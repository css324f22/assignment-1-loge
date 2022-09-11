import copy


def initial_state():
    return ((6, 9, 8, 7, 1, 3, 2, 5, 4), 0, 1)


def is_goal(s):
    for i in range(0, 9, 3):
        if s[0][i] + s[0][i+1]+s[0][i+2] != 15:
            return False
    for i in range(3):
        if s[0][i] + s[0][i+3]+s[0][i+6] != 15:
            return False
    if s[0][2] + s[0][4] + s[0][8] != 15:
        return False

    if s[0][2] + s[0][4] + s[0][6] != 15:
        return False

    return True


def successors(s):
    _, r, c = s
    #move up
    new_r, new_c = r-1, c
    if is_valid(new_r, new_c):
        yield move_nine(s, new_r, new_c), 1
    #move down
    new_r, new_c = r + 1, c
    if is_valid(new_r, new_c):
        yield move_nine(s, new_r, new_c), 1
    #move left
    new_r, new_c = r, c-1
    if is_valid(new_r, new_c):
        yield move_nine(s, new_r, new_c), 1
    #move right
    new_r, new_c = r, c+1
    if is_valid(new_r, new_c):
        yield move_nine(s, new_r, new_c), 1


def is_valid(r, c):
    return 0 <= r <= 2 and 0 <= c <= 2


def move_nine(s, new_r, new_c):
    board, r, c = s
    new_board = list(board)
    new_board[r*3 + c] = new_board[new_r*3 + new_c]
    new_board[new_r*3 + new_c] = 0
    return (tuple(new_board), new_r, new_c)
