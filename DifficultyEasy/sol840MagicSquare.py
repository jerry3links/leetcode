"""
    from DifficultyEasy.sol840MagicSquare import Solution
    grid = [[4,3,8,4],
            [9,5,1,9],
            [2,7,6,2]]
    ans = Solution().numMagicSquaresInside(grid)
    print("ans: {}".format(ans))
"""


class Solution(object):

    SQR_DIM = 3

    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_row = len(grid)

        if num_row < self.SQR_DIM or num_row <= 0:
            return 0

        num_col = len(grid[0])

        if num_col < self.SQR_DIM or num_col <= 0:
            return 0

        # print("row: {}".format(num_row))
        # print("col: {}".format(num_col))

        cnt = 0

        for i in range(num_row - (self.SQR_DIM - 1)):
            for j in range(num_col - (self.SQR_DIM - 1)):
                square = [row[j:j+self.SQR_DIM] for row in grid[i:i+self.SQR_DIM]]

                # print("SQ")

                if self.isMagicSquare(square):
                    cnt += 1

        return cnt

    def isMagicSquare(self, square):

        lst = set()
        for i in range(self.SQR_DIM):
            for j in range(self.SQR_DIM):
                val = square[i][j]
                if val < 1 or val > 9:
                    return False
                lst.add(val)
        if len(lst) != 9:
            return False




        base = None
        for row in square:
            print(row)
            if not base:
                base = sum(row)
            else:
                if sum(row) != base:
                    return False

        col0 = [v[0] for v in square]
        if sum(col0) != base:
            return False
        col1 = [v[1] for v in square]
        if sum(col1) != base:
            return False
        col2 = [v[2] for v in square]
        if sum(col2) != base:
            return False

        dag0 = square[0][0] + square[1][1] + square[-1][-1]
        if dag0 != base:
            return False
        dag1 = square[0][-1] + square[1][1] + square[-1][0]
        if dag1 != base:
            return False

        return True
