
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """



        def get_neighbours(i, j, m, n):

            h_ind_1 = (i + 0, j - 1)
            h_ind_2 = (i + 0, j + 1)

            v_ind_1 = (i + 1, j + 0)
            v_ind_2 = (i - 1, j + 0)

            f_ind_1 = (i - 1, j - 1)
            f_ind_2 = (i - 1, j + 1)

            o_ind_1 = (i + 1, j - 1)
            o_ind_2 = (i + 1, j + 1)

            indices_list = [
                h_ind_1, h_ind_2, 
                v_ind_1, v_ind_2, 
                f_ind_1, f_ind_2, 
                o_ind_1, o_ind_2
            ]

            neighbour_list = []

            for curr_ind in indices_list:
                i, j = curr_ind
                if check_ind_validity(i, j, m, n):
                    neighbour_list.append(curr_ind)
            
            return neighbour_list
        

        def check_ind_validity(i, j, m, n):
            # print(f"{i=}, {j=}")
            # print(f"{m=}, {n=}")
            return (i >= 0) and (j >= 0) and (i <= m - 1) and (j <= n - 1)

        def get_live_neighbour_count(neighbour_list):
            
            live_n_count = 0

            for i, j in neighbour_list:
                print(f"{i=}, {j=}")
                print(f"{board[i][j]=}")
                live_n_count += board[i][j]

            # return sum([board[i][j] for i, j in neighbour_list])
            return live_n_count
        
        m = len(board)
        n = len(board[0])
        
        board_copy = [[0 for _ in range(n)] for _ in range(m)]
        
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                neighbour_list = get_neighbours(i, j, m, n)
                live_n_count = get_live_neighbour_count(neighbour_list)
                if col:
                    if live_n_count < 2:
                        board_copy[i][j] = 0
                    elif live_n_count >=2 and live_n_count <= 3:
                        board_copy[i][j] = col
                    elif live_n_count > 3:
                        board_copy[i][j] = 0
                    else:
                        board_copy[i][j] = col
                else:
                    if live_n_count == 3:
                        board_copy[i][j] = 1
                    else:
                        board_copy[i][j] = col

        print(f"{board_copy=}")
        print(f"{board=}")

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                board[i][j] = board_copy[i][j]
                
        
        board = board_copy
        print(f"{board=}")

if __name__ == "__main__":

    # board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

    Solution().gameOfLife(board)
    print(board)
    # [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    # board = [[1,1],[1,0]]
    # Solution().gameOfLife(board)
    # print(board)
    
