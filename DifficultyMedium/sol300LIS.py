"""
    from DifficultyMedium.sol300LIS import Solution
    nums = [10,9,2,5,3,7,101,18]
    ans = Solution().lengthOfLIS(nums)
    print(ans)
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        if L < 1:
            return 0

        LIS = 0

        rmap = {}
        min_val = float("inf")
        for i in range(len(nums)):
            if nums < min_val:
                min_val = num



        lmap = [[min(nums)] for v in nums]

        print(lmap)


        for length in range(2, L + 1):
            print("length: {}".format(length))

            for num in nums:
                if lmap[length - 1][-1] < num:
                    lmap[length - 1].append(num)

        return LIS



