"""
    from BitManipulation.solM137SingleNumII import Solution
    nums = [2,2,3,2]
    nums = [0,1,0,1,0,1,99]
    nums = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
    print("nums: {}".format(nums))
    ans = Solution().singleNumber(nums)
    print("ans = {}".format(ans))
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        



    def secondImpl(self, nums):
        d = {}

        for val in nums:
            if val in d:
                d[val] += 1
            else:
                d[val] = 1

        for k in d:
            if d[k] == 1:
                return k

    # only works for positive numbers
    def firstImpl(self, nums):

        result = 0
        count = [0 for _ in range(32)]
        for i in range(32):
            for j in range(len(nums)):
                if (nums[j] >> i) & 1 == 1:
                    count[i] += 1
            result |= count[i] % 3 << i
            # print("{} ({}) ...".format(result, bin(result)))
        return result