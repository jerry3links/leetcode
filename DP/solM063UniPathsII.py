"""
    from DP.solM063UniPathsII import Solution
    input = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    # input = [
    #     [1],
    #     [0]
    # ]
    print("input:\n{}".format(input))
    ans = Solution().uniquePathsWithObstacles(input)
    print("ans = {}".format(ans))
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)

        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(m):
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
                break
            else:
                dp[0][i] = 1

        for j in range(n):
            if obstacleGrid[j][0] == 1:
                dp[j][0] = 0
                break
            else:
                dp[j][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if dp[i - 1][j] > 0 and dp[i][j - 1] > 0:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    elif dp[i - 1][j] == 0:
                        dp[i][j] = dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]