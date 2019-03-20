"""
    from BinarySearch.solE035SearchInsert import Solution
    # nums = [1,3,5,6]; target = 5
    # nums = [1, 3, 5, 6]; target = 2
    # nums = [1, 3, 5, 6]; target = 7
    # nums = [1, 3, 5, 6]; target = 0
    # nums = [1, 3]; target = 4
    nums = [1, 3]; target = 2
    print("nums: {}, target = {}".format(nums, target))
    ans = Solution().searchInsert(nums, target)
    print("ans = {}".format(ans))
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L = 0
        R = len(nums) - 1
        while L < R:
            M = int((L + R) / 2)
            if target > nums[M]:
                L = M + 1
            else:
                R = M

        return L if target <= nums[L] else L + 1
