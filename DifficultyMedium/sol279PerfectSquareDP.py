"""Put the following in main of demo,py
    from DifficultyMedium.sol279PerfectSquareDP import Solution
    n_lst = [0, 1, 12, 13]
    for n in n_lst:
        print("n: {}".format(n))
        a = Solution().numSquares(n)
        print("num of ps: {}".format(a))
"""


class Solution:
    def numSquares(self, n):
        if n < 2:
            return n
        lst = [i * i for i in range(1, n + 1)]
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0

        for num in lst:
            for i in range(num, n + 1):
                dp[i] = min(dp[i], dp[i - num] + 1)

        best = dp[-1]

        if best == float("inf"):
            return 0

        return best