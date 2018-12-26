"""
    # time: O(n*logn)
    from Rethink.sol167TwoSumII import Solution
    numbers = [2,7,11,15]; target = 9
    print("numbers: {}, target: {}".format(numbers, target))
    ans = Solution().twoSum(numbers, target)
    print("ans = {}".format(ans))
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) <= 1:
            return []

        # v2i_map = {}
        for i in range(len(numbers)):
            j = self.bsearch(numbers, target - numbers[i], i + 1)
            if j != -1:
                return [i+1, j+1]

        return []

    def bsearch(self, numbers, key, start):
        L = start
        R = len(numbers) - 1

        while L < R:
            M = int((L + R) / 2)
            if numbers[M] < key:
                L = M + 1
            else:
                R = M

        if L == R and numbers[L] == key:
            return L
        else:
            return -1

