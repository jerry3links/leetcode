"""
    from DifficultyMedium.solM539MinimumTimeDiff import Solution
    timePoints = ["23:59","00:00"]
    print("timePoints: {}".format(timePoints))
    ans = Solution().findMinDifference(timePoints)
    print("ans: {}".format(ans))
"""



class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        times_a = sorted([int(s[:2]) * 60 + int(s[3:]) for s in timePoints])
        times_b = times_a[1:] + [times_a[0] + 1440]
        return min(b-a for a, b in zip(times_a, times_b))


    # NOTE: TLE
    def firstImple(self, timePoints):
        import itertools
        tp_pairs = itertools.combinations(list(range(len(timePoints))), 2)

        min_diff = float("inf")
        for pair in tp_pairs:
            a = int(timePoints[pair[0]][:2]) * 60 + int(int(timePoints[pair[0]][3:]))
            b = int(timePoints[pair[1]][:2]) * 60 + int(int(timePoints[pair[1]][3:]))
            diff = a - b if a > b else b - a
            if diff > 720:
                diff = (1440 - diff) % diff

            if diff < min_diff:
                min_diff = diff
        return min_diff

