"""
from sol045JumpGame import Solution
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
        # FAIL TO IMPLEMENT
        tab = [0 for v in nums]
        L = len(nums)
        D = L - 1

        for i in range(L):
            go = i
            cnt = 1
            flag = True
            n = nums[i]
            while flag:
                if go == D:
                    tab[i] = cnt
                    break
                go += n
                cnt += 1
        print(tab)





        return -1
