class Solution:
    def is_valid_point(self, board: [[str]], x: int, y: int) -> bool:
        if x < 0 or x > len(board)-1 or y < 0 or y > len(board[0])-1:
            return False
        return board[x][y] == 'X'

    def countBattleships(self, board: [[str]]) -> int:
        ships = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and not self.is_valid_point(board, i+1, j) and not self.is_valid_point(board, i, j+1):
                    ships += 1
        return ships


board1 = [["X",".",".","."],["X",".",".","."],["X",".",".","."]]
s = Solution()
print(s.countBattleships(board1))
