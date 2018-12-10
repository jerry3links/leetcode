"""
    from DifficultyMedium.sol1011Container import Solution
    height = [1,8,6,2,5,4,8,3,7]
    a = Solution().maxArea(height)
    print("ans: {}".format(a))
"""

class Solution:
    def maxArea(self, height, result = 0, L = 0):
        if not height: return 0
        R = len(height)-1
        while L != R:
            result = max(result, min(height[L], height[R])*(R-L))
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return result