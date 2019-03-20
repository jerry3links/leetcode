"""
    from BinarySearch.solM153FindMin import Solution
    input = [3,4,5,1,2]
    print("input: {}".format(input))
    ans = Solution().findMin(input)
    print("ans = {}".format(ans))
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        L = 0
        R = len(nums) - 1

        while L < R: # nums[L] > nums[R]
            M = int((L + R) / 2)
            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M
        return nums[L]


