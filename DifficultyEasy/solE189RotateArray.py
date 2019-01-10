"""
    from DifficultyEasy.solE189RotateArray import Solution
    nums = [1,2,3,4,5,6,7]; k = 3
    # nums = [-1,-100,3,99]; k = 2
    nums = [1, 2]; k = 3
    print("nums: {}, k = {}".format(nums, k))
    Solution().rotate(nums, k)
    print("ans: {}".format(nums))

"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if k >= len(nums):
            k = k % len(nums)

        if k == 0:
            return

        head = nums[-k:]
        tail = nums[:len(nums) - k]

        i = 0
        for v in head:
            nums[i] = v
            i+=1
        for v in tail:
            nums[i] = v
            i+=1

