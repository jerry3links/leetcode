"""
    from BitManipulation.solE136SingleNum import Solution
    nums = [2,2,1]
    nums = [4,1,2,1,2]
    print("nums: {}".format(nums))
    ans = Solution().singleNumber(nums)
    print("ans = {}".format(ans))

"""


class Solution(object):

    # time: 99%, space: 7.6%
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        base = 0
        for v in nums:
            base ^= v
        return base


    # time: 71%, space: 0.98%
    def secondImplSet(self, nums):
        numSet = set()
        for val in nums:
            if val in numSet:
                numSet.remove(val)
            else:
                numSet.add(val)

        return numSet.pop()

    # time: 71%, space: 0.98%
    def firstImplMap(self, nums):
        numMap = {}

        for val in nums:
            if val not in numMap:
                numMap[val] = 1
            else:
                numMap[val] += 1

        for key in numMap.keys():
            if numMap[key] == 1:
                return key
