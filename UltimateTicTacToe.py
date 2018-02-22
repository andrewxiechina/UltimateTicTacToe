from __future__ import print_function

# Constants
N = 9
PLAYER_1 = 1
PLAYER_2 = 2
EMPTY = 0
PRINT_DICT = {0:"-", 1:"X", 2:"O"}
TIE = 0
NO_WINNER = -1
INPUT_DICT = {7:0, 8:1, 9:2, 4:3, 5:4, 6:5, 1:6, 2:7, 3:8}

def init_board():
    return [0 for i in range(N)]

def draw_board(board):
    print("\n\t", PRINT_DICT[board[0]], "|", PRINT_DICT[board[1]], "|",PRINT_DICT[board[2]])
    print("\t", "---------")
    print("\t", PRINT_DICT[board[3]], "|", PRINT_DICT[board[4]], "|",PRINT_DICT[board[5]])
    print("\t", "---------")
    print("\t", PRINT_DICT[board[6]], "|", PRINT_DICT[board[7]], "|", PRINT_DICT[board[8]], "\n")

def draw_board_(board):
    """Display function sued for testing only"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def winner(board):
    """Return winner 1/2, return TIE or NO_WINNER otherwise."""
    WAYS_TO_WIN = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

        if EMPTY not in board:
            return TIE

        return NO_WINNER

def move(board, pos, player):
    assert (board[pos] == EMPTY), "The position is illegal, occupied by another piece"
    board[pos] = player

def init_ultimate_board():
    return [init_board() for i in range(N)]

def ultimate_winner(ultimate_board):
    winners = [-1 for i in range(N)]
    for i in range(len(ultimate_board)):
        winners[i] = winner(ultimate_board[i])
    return winner(winners) # Feed in winners as a new board

def ultimate_move(ultimate_board, ultimate_board_pos, pos, player):
    move(ultimate_board[ultimate_board_pos], pos, player)

def ultimate_draw_row(rows):
    for row in rows:
        print(" ", PRINT_DICT[row[0]], "|", PRINT_DICT[row[1]], "|", PRINT_DICT[row[2]], end="")
        print("\t", end="")
    print()

def ultimate_draw_board(ultimate_board):
    import os
    os.system('clear')
    seperator = " -----------\t ----------\t  -----------  "
    b = ultimate_board
    for i in range(3):
        print()
        for j in range(3):
            print("\t", end="")
            ultimate_draw_row((b[i*3][j*3:j*3+4], b[i*3+1][j*3:j*3+4], b[i*3+2][j*3:j*3+4]))
            print("\t", end="")
            if j % 3 != 2: print(seperator)
        print()


if __name__ == "__main__":
    # Unit Tests
    # board = init_board()
    # draw_board(board)
    # board[3] = 1
    # board[5] = 2
    # draw_board(board)
    # print(winner(board))
    # move(board, 4, 1)
    # draw_board(board)

    # Unit Tests for Ultimate
    # u_board = init_ultimate_board()
    # ultimate_draw_board(u_board)

    board = init_ultimate_board()
    player = PLAYER_1
    ultimate_draw_board(board)
    while(True):
        x, y = input()
        x = INPUT_DICT[x]
        y = INPUT_DICT[y]

        ultimate_move(board, x, y, player)
        ultimate_draw_board(board)

        win = ultimate_winner(board)
        if(win == PLAYER_1 or win == PLAYER_2):
            "You WIN!!"
        elif(win == TIE):
            "TIE!!"

        if player is PLAYER_1:
            player = PLAYER_2
        else:
            player = PLAYER_1
