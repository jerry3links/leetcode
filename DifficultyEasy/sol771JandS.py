"""
    from DifficultyEasy.sol771JandS import Solution
    J = "aA"
    S = "aAAbbbb"
    ans = Solution().numJewelsInStones(J, S)
    print("J: {}, S: {}".format(J, S))
    print("ans: {}".format(ans))
"""


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        jset = set(J)
        slst = list(S)

        res = 0
        for v in jset:
            res += slst.count(v)

        return res
