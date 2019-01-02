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
        # initialize
        f = [[[] for _ in range(target+1)] for _ in range(len(candidates))]

        # there is no combination for ZERO
        for i in range(len(candidates)):
            f[i][0] = [[]]

        # only one type of COIN, concatenate if there exists combination
        for amount in range(1, target + 1):
            remain = amount - candidates[0]
            if remain == 0:
                f[0][amount] = [[candidates[0]]]
            elif remain > 0 and len(f[0][remain]) > 0:
                f[0][amount] = [f[0][remain][0] + [candidates[0]]]

        for i in range(1, len(candidates)):

            # print("for COINS set {} ...".format(candidates[:i+1]))

            for amount in range(1, target + 1):
                remain = amount - candidates[i]

                # includes previous COINS set
                if len(f[i - 1][amount]) > 0:
                    f[i][amount] = list(f[i - 1][amount])

                if remain == 0:
                    # current COIN is equal to the target amount
                    f[i][amount].append([candidates[i]])
                elif remain > 0:
                    # check if there exists combinations for remain value
                    for base in f[i][remain]:
                        tmp = list(base) + [candidates[i]]
                        f[i][amount].append(tmp)

        # self.printout(f)
        return f[-1][-1]

    def printout(self, f):
        for i, row in zip(range(len(f)), f):
            dbg = [len(v) for v in row]
            # print("{}: {}".format(i, dbg))
            print("{}: {}".format(i, row))