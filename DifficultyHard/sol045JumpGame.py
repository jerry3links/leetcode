"""
from DifficultyHard.sol045JumpGame import Solution
nums = [2,3,1,1,4]
ans = Solution().jump(nums)
print(ans)
"""


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        curr_reach = next_reach = cnt = i = 0
        while True:
            while i <= curr_reach:
                next_reach = max(i+nums[i], next_reach)
                if next_reach >= len(nums) - 1:
                    return cnt + 1
                i += 1
            curr_reach = next_reach
            cnt += 1

    def toTarget(self, nums):
        """
        DP-like solution
        """
        L = len(nums)
        if L <= 1:
            return 0

        D = L - 1

        dp = []
        target = 0
        for i in range(L):
            dp.append(i + nums[i])
            if dp[i] >= D:
                target = i
                break

        cnt = 1
        while target != 0:
            i = 0
            while i < target:
                if dp[i] >= target:
                    target = i
                    break
                i = i + 1
            cnt += 1

        return cnt
