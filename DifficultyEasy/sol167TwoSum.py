"""
    from DifficultyEasy.sol167TwoSum import Solution
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

        v2i_map = {}
        for i in range(len(numbers)):

            if (target - numbers[i]) in v2i_map:
                return [v2i_map[target - numbers[i]] + 1, i + 1]

            v2i_map[numbers[i]] = i

        return []