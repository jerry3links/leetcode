"""
    from DifficultyMedium.sol054MSpiralMatrix import Solution
    matrix = [[1,2,3],[4,5,6],[6,8,9]]
    ans = Solution().spiralOrder(matrix)
    print("ans: {}".format(ans))
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        seq = []
        m = len(matrix)
        if m <= 0:
            return []
        n = len(matrix[0])

        row = 0
        col = -1
        while True:
            for _ in range(n):
                col += 1
                seq.append(matrix[row][col])

            m -= 1
            if m == 0:
                break

            for _ in range(m):
                row += 1
                seq.append(matrix[row][col])

            n -= 1
            if n == 0:
                break

            for _ in range(n):
                col -= 1
                seq.append(matrix[row][col])

            m -= 1
            if m == 0:
                break

            for _ in range(m):
                row -= 1
                seq.append(matrix[row][col])

            n -= 1
            if n == 0:
                break

        return seq