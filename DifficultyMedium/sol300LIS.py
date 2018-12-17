"""
    from DifficultyMedium.sol300LIS import Solution
    # nums = [10,9,2,5,3,7,101,18]
    # nums = [10, 9, 2, 5, 3, 4]
    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    ans = Solution().lengthOfLIS(nums)
    print(ans)
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        T = [1 for i in range(len(nums))]
        LIS = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    T[i] = max(T[i], T[j] + 1)
            if T[i] > LIS:
                LIS = T[i]

        return LIS

