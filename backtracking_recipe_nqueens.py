
from collections import namedtuple

# m -- matrix representing the chessboard
# we use 0 to represent an open square and 1 to represent a queen
# n -- the required number of queens
# nq -- the number of queens currently on the board
Board = namedtuple("Board", ["m","nq","n"])
finished = False

def nqueen(n):
    # starting off with an empty chessboard
    board = Board(m = [[0]*n for _ in range(n)], nq = 0, n = n)
    backtrack(board)

def is_a_solution(board):
    return board.nq == board.n

# We print the configuration and turn off the backtrack search by setting off the global finished flag on finding a solution:

def process_solution(board):
    for row in board.m:
        print(row)
    global finished
    finished = True

# Constructing the candidates for the next solution position involves finding all the open squares where the queen cannot be attacked:

# Let (x, y) be the square we are checking for legality

def any_queen_in_row(board, x):
    return any(elem == 1 for elem in board.m[x])

def any_queen_in_column(board, y):
    return any(board.m[i][y] == 1 for i in range(board.n))

def any_queen_in_diag(board, x, y):
    xs_down = range(x + 1, board.n)    # rows below (x, y)
    xs_up = range(x - 1, -1, -1)       # rows above (x, y)
    ys_right = range(y + 1, board.n)   # columns to the right of (x, y)
    ys_left = range(y-1, -1, -1)       # columns to the left of (x, y)
    diag_1 = list(zip(xs_up, ys_right)) + list(zip(xs_down, ys_left))
    diag_2 = list(zip(xs_up, ys_left)) + list(zip(xs_down, ys_right))
    diag = diag_1 + diag_2
    return any(board.m[d_x][d_y] == 1 for (d_x, d_y) in diag)

def square_is_legal(board, x, y):
    return (not any_queen_in_row(board, x)
            and not any_queen_in_column(board, y)
            and not any_queen_in_diag(board, x, y))

def construct_candidates(board):
    candidate_list = []
    for x in range(board.n):
        for y in range(board.n):
            if square_is_legal(board, x, y):
                candidate_list.append((x, y))
    return candidate_list

# We must update our board data structure to reflect the effect of putting a queen on a chessboard square, as well as remove these changes should we backtrack away from this move. These updates are handled by make_move and unmake_move, both of which are called directly from backtrack:

def make_move(board, x, y):
    m = board.m
    nq = board.nq
    m[x][y] = 1
    nq += 1
    return Board(m = m, nq = nq, n = board.n)

def unmake_move(board, x, y):
    m = board.m
    nq = board.nq
    m[x][y] = 0
    nq -= 1
    return Board(m = m, nq = nq, n = board.n)

def backtrack(board):
    if is_a_solution(board):
        process_solution(board)
    else:
        candidate_list = construct_candidates(board)
        for (x, y) in candidate_list:
            board = make_move(board, x, y)
            backtrack(board)
            board = unmake_move(board, x , y)
            global finished
            if finished: return

nqueen(5)

