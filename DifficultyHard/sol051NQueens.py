"""
    from DifficultyHard.sol051NQueens import Solution
    n = 4
    ans = Solution().solveNQueens(n)
    print(ans)
"""


class Solution(object):

    N = 0

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 1:
            return [['Q']]
        if n < 4:
            return []
        self.N = n

        ans = []
        board = [["." for _ in range(self.N)] for _ in range(self.N)]
        self.solve(0, board, ans)

        return ans

    def solve(self, x, board, fixed_boards):

        if x == self.N:
            # print("one sol:{}".format(board))

            fixed = []
            for row in board:
                fixed.append("".join(row))
            fixed_boards.append(fixed)
            return

        for y in range(self.N):
            if not self.isSafe(board, x, y): continue
            board[x][y] = "Q"
            # print("board[x]: {}".format(board[x]))
            self.solve(x+1, board, fixed_boards)
            board[x][y] = "."

        return

    def isSafe(self, board, x, y):

        # check column y
        for i in range(x):
            if board[i][y] == "Q":
                return False

        # check diagonal (backslash: \)
        for i, j in zip(range(x-1, -1, -1), range(y-1, -1, -1)):
            if board[i][j] == "Q":
                return False

        # check diagonal (slash: /)
        for i, j in zip(range(x-1,-1,-1), range(y+1, self.N)):
            if board[i][j] == "Q":
                return False

        return True
