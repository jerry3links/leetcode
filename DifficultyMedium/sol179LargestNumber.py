"""
    from DifficultyMedium.sol179LargestNumber import Solution
    nums = [3,30,34,5,9]
    a = Solution().largestNumber(nums)
    print("ans: {}".format(a))
    nums = [0]
    a = Solution().largestNumber(nums)
    print("ans: {}".format(a))
    nums = [0,0]
    a = Solution().largestNumber(nums)
    print("ans: {}".format(a))
"""


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        for i in range(len(nums)):

            for j in range(len(nums) - i - 1):
                a = str(nums[j])
                b = str(nums[j+1])

                if int(a + b) > int(b + a):
                    continue
                else:
                    nums[j] = int(b)
                    nums[j+1] = int(a)

        zeros = [v for v in nums if v == 0]

        if len(zeros) == len(nums):
            return "0"

        s = ""
        for v in nums:
            s += str(v)

        return s