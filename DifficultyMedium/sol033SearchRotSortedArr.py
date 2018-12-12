"""
    from DifficultyMedium.sol033SearchRotSortedArr import Solution
    nums = [4,5,6,7,0,1,2]
    target = 0
    ans = Solution().search(nums, target)
    print(ans)
"""
class Solution:
    def search(self, nums, target, rotated = True):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # idxMap = {}
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i

        head, tail = 0, len(nums) - 1

        while head <= tail:

            midd = int((tail + head)/2)
            if target == nums[midd]:
                return midd

            if nums[midd] >= nums[head]:
                if nums[midd] >= target >= nums[head]:
                    tail = midd
                else:
                    head = midd + 1
            else:
                if nums[tail] >= target >= nums[midd]:
                    head = midd
                else:
                    tail = midd - 1

        return -1
