"""
    from DifficultyEasy.solE263UglyNumber import Solution
    num = 6
    print("num: {}".format(num))
    ans = Solution().isUgly(num)
    print("ans: {}".format(ans))
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        bases = [2,3,5]

        Q = [num]

        while Q:

            target = Q.pop(0)

            if target == 1:
                return True

            for b in bases:
                if target % b == 0:
                    Q.append(target / b)
                    break

        return False


