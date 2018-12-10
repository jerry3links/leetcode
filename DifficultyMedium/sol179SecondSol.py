"""
    from DifficultyMedium.sol179SecondSol import Solution
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

        # map will return nums' iterable using str()
        nums = map(str,nums)
        # sort list using self defined cmp, and using descending order
        nums.sort(cmp=lambda a,b : cmp(a+b,b+a), reverse=True)

        # join vs split
        # note the A or B, will return B if A is empty string
        return ''.join(nums).lstrip('0') or '0'