
board1 = [["X",".",".","."],["X",".",".","."],["X",".",".","."]]

def is_valid(board, i, j):
    if i < 0 or i > len(board)-1 or j < 0 or j > len(board)-1:
        return False
    return board[i][j] == 'X'


def process_board(board):
    ships = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'X' and not is_valid(board, i+1, j) and not is_valid(board, i, j+1):
                ships += 1
    return ships

print(process_board(board1))
