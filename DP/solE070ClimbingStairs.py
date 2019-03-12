"""
    from DP.solE070ClimbingStairs import Solution
    input = 2
    print("input: {}".format(input))
    ans = Solution().climbStairs(input)
    print("ans = {}".format(ans))
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        f = [0 for _ in range(n + 1)]

        for i in range(3):
            f[i] = i

        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[-1]

