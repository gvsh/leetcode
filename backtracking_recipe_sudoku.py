



from collections import namedtuple

Board = namedtuple("Board", ["m","freecount"])
# matrix of board contents
# we use 0 to represent an open square
m = [[3,0,6,5,0,8,4,0,0],
     [5,2,0,0,0,0,0,0,0],
     [0,8,7,0,0,0,0,3,1],
     [0,0,3,0,1,0,0,8,0],
     [9,0,0,8,6,3,0,0,5],
     [0,5,0,0,9,0,6,0,0],
     [1,3,0,0,0,0,2,5,0],
     [0,0,0,0,0,0,0,7,4],
     [0,0,5,2,0,6,3,0,0]]

# how many open squares remain?
freecount = sum(1 for row in m for elem in row if elem == 0)
board = Board(m = m, freecount = freecount)

def next_square(board):
    for row in range(9):
        for column in range(9):
            if board.m[row][column] == 0:
                return (row, column)
    return ()


"""

Next, we need to identify which numbers are candidates to fill that square (possible_values). 
The candidates to fill the open square (i,j)

are:

    U−(R∪C∪S) where :


U={1,2,3,4,5,6,7,8,9}
R={x∣x exists in row i}
C={x∣x exists in column j}
S={x∣x exists in (i, j)'s sector}
"""

# returns the top-left corner 
# of the 3 × 3 sector containing (x, y)
def sector_top_left(x, y):
    return ((x // 3) * 3, (y // 3) * 3)

def possible_values(board, x, y):
    (s_x, s_y) = sector_top_left(x, y)
    universal_set = set(range(1,10))
    row_set = set(board.m[x])
    column_set = {board.m[i][y] for i in range(9)}
    sector_set = {board.m[i+s_x][j+s_y] for i in range(3) for j in range(3)}
    union_set = (row_set | column_set | sector_set)
    return universal_set - union_set

# We must update our board data structure to reflect the 
# effect of filling a candidate value into a square, 
# as well as remove these changes should we backtrack away from this position. 
# These updates are handled by make_move and unmake_move, 
# both of which are called directly from backtrack:

def make_move(board, x, y, value):
    m = board.m
    freecount = board.freecount
    m[x][y] = value
    freecount -= 1
    return Board(m = m, freecount = freecount)

def unmake_move(board, x, y):
    m = board.m
    freecount = board.freecount
    m[x][y] = 0
    freecount += 1
    return Board(m = m, freecount = freecount)

# One important job for these board update routines is 
# maintaining how many free squares remain on the board. 
# A solution is found when there are no more free squares remaining to be filled:

def is_a_solution(board):
    return board.freecount == 0

# The rest of the program is:

def process_solution(board):
    for row in board.m:
        print(row)

def construct_candidates(board):
    (x, y) = next_square(board)
    value_set = possible_values(board, x, y)
    if value_set:
        return {(x, y, value) for value in value_set}
    else:
        return set()

def backtrack(board):
    if is_a_solution(board):
        process_solution(board)
    else:
        candidate_list = construct_candidates(board)
        for x, y, value in candidate_list:
            board = make_move(board, x, y, value)
            backtrack(board)
            board = unmake_move(board, x , y)

def sudoku_solver(board):
    backtrack(board)

if __name__ == "__main__":
    sudoku_solver(board)
