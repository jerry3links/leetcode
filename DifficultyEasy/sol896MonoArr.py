"""
    from DifficultyEasy.sol896MonoArr import Solution
    A = [1,2,2,3]
    A = [1, 1, 1, 2, 2, 3, 2, 1]
    A = [1, 1, 1, 2, 2, 3]
    # A = [1, 1, 1, 2]
    # A = [1, 1, 1]
    print(A)
    ans = Solution().isMonotonic(A)
    print("ans: {}".format(ans))
"""


class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        isMono = True
        if len(A) < 2:
            # print("edge case")
            return isMono

        beg = 0
        for i in range(len(A) - 1):
            if A[i] != A[i + 1]:
                beg = i + 1
                break

        # print("stop @ {}".format(beg))

        begIncreasing = False
        if beg == len(A) - 1:
            # print("all the same until end")
            return isMono
        elif A[beg] > A[beg - 1]:
            begIncreasing = True

        if begIncreasing:
            # print("begIncreasing")
            for i in range(beg, len(A) - 1):
                if A[i] > A[i+1]:
                    isMono = False
                    break
        else:
            for i in range(beg, len(A) - 1):
                if A[i] < A[i+1]:
                    isMono = False
                    break
        return isMono