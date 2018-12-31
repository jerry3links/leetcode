"""
    from DifficultyMedium.solM039CombSum import Solution
    candidates = [2,3,6,7]; target = 7
    print("candidates: {}; target: {}".format(candidates, target))
    ans = Solution().combinationSum(candidates, target)
    print(ans)
"""

# Note: all possible sets (not number of sets)
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target <= 0:
            return []

        candidates.sort()
        f = [[[]] * (target + 1) for _ in range(len(candidates))]

        for i in range(len(candidates)):
            # print(candidates[:i+1])
            # a = [amount for amount in range(1, target + 1)]
            for amount in range(1, target + 1):
                f[i][amount] =

        self.printout(f)

    def printout(self, f):
        for row in f:
            print(row)