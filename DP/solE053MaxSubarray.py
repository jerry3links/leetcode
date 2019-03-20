"""
    from DP.solE053MaxSubarray import Solution
    input = [-2,1,-3,4,-1,2,1,-5,4]
    print("input: {}".format(input))
    ans = Solution().maxSubArray(input)
    print("ans = {}".format(ans))
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        f = [0 for _ in range(len(nums))]

        res = f[0] = nums[0]

        for i in range(1, len(nums)):
            f[i] = max(nums[i] + f[i-1], nums[i])
            res = max(res, f[i])

        print(f)

        return res