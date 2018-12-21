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

        boards = []

        targets = [(0, 0)]

        while targets:
            x, y = targets.pop()
            # print("Start from <{}, {}>".format(x, y))
            ckboard = self.solveFromXY(x, y)
            if len(ckboard) == 0:
                continue

            for i in range(self.N):
                if ckboard[0][i] == '-':
                    targets.append((0, i))
                    break

            asboard = []
            for row in ckboard:
                asboard.append("".join(row).replace("-", "."))
            boards.append(asboard)

        return boards

    def solveFromXY(self, x = 0, y = 0, DEBUG = False):

        ckboard = [["-" for _ in range(self.N)] for _ in range(self.N)]

        # for j in range(y, self.N):
        #     ckboard[x][j] = "-"
        #
        # for i in range(x + 1, self.N):
        #     for j in range(self.N):
        #         ckboard[i][j] = "-"

        if DEBUG:
            print("Begin from ckboard:\n{}".format(ckboard))

        stack = []

        row = 0
        while row < self.N:

            # print("BEGIN - FOR ROW {}".format(row))
            if self.solveRow(ckboard, row, stack):
                # print("END - found!")
                row += 1
            else:
                if len(stack) == 0:
                    # print("IMPOSSIBLE")
                    return []

                row_prv, col_prv = stack.pop()
                self.resetBoardFromXY(ckboard, row_prv, col_prv)
                ckboard[row_prv][col_prv] = "."
                # print("END - not found, will rerun from <{}, {}>".format(row_prv, col_prv))
                row = row_prv
                continue

        # print("stack: {}".format(stack))
        if DEBUG:
            print("Done! ckboard:\n{}".format(ckboard))

        return ckboard


    def solveRow(self, board, i, stack):

        for j in range(self.N):
            if board[i][j] == ".": # . = visited
                continue
            elif board[i][j] == "-":
                board[i][j] = "."
            if self.isSafe(board, i, j):
                board[i][j] = "Q"
                stack.append((i, j))
                return True

        return False

    def resetBoardFromXY(self, board, x, y):

        for j in range(y, self.N):
            board[x][j] = "-"

        for i in range(x + 1, self.N):
            for j in range(self.N):
                board[i][j] = "-"

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
