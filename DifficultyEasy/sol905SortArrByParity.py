"""
    from DifficultyEasy.sol905SortArrByParity import Solution
    A = [3,1,2,4]
    print("A: {}".format(A))
    ans = Solution().sortArrayByParity(A)
    print("ans: {}".format(ans))
"""
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        evn = []
        for num in A:
            if num % 2 == 0:
                odd.append(num)
            else:
                evn.append(num)

        ans = odd + evn


        return ans