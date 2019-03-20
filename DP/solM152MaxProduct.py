"""
    from DP.solM152MaxProduct import Solution
    input = [2,3,-2,4]
    print("input: {}".format(input))
    ans = Solution().maxProduct(input)
    print("ans = {}".format(ans))

"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        pos = [0 for _ in range(len(nums))]
        neg = [0 for _ in range(len(nums))]
        res = pos[0] = neg[0] = nums[0]

        for i in range(1, len(nums)):
            pos[i] = max(nums[i], pos[i-1] * nums[i], neg[i-1] * nums[i])
            neg[i] = min(nums[i], pos[i-1] * nums[i], neg[i-1] * nums[i])
            res = max(res, pos[i])

        return res




