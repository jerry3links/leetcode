"""
    # time: O(n)
    from Rethink.sol167TwoSumIIPointer import Solution
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

        L = 0
        R = len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] == target:
                return [L+1, R+1]
            elif numbers[L] + numbers[R] > target:
                R -= 1
            else:
                L += 1

        return []
