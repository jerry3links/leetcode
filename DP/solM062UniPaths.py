"""
    from DP.solM062UniPaths import Solution
    m, n = 3, 2
    print("m = {}, n = {}".format(m,n))
    ans = Solution().uniquePaths(m, n)
    print("ans = {}".format(ans))
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ones = [1 for _ in range(m)]
        zros = [1] + [0 for _ in range(m - 1)]
        dp = [ones]
        for _ in range(n-1):
            dp.append(zros)

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

