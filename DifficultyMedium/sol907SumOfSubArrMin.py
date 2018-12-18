"""
    # Input: [3,1,2,4]
    # Output: 17
    # Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]

    from DifficultyMedium.sol907SumOfSubArrMin import Solution
    A = [3,1,2,4]
    # A = [2,9,7,8,3,4,6,1]
    print("A: {}".format(A))
    ans = Solution().sumSubarrayMins(A)
    print(ans)
"""

class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 1:
            return 0

        lft = [i + 1 for i in range(len(A))]
        rht = [len(A) - i for i in range(len(A))]

        stk_ple = []
        stk_nle = []


        for i in range(len(A)):
            # for PLE
            while len(stk_ple) > 0 and stk_ple[-1] > A[i]:
                stk_ple.pop()
                stk_ple.pop()
            lft[i] = i + 1 if len(stk_ple) <= 0 else i - stk_ple[-2]
            stk_ple.append(i)
            stk_ple.append(A[i])
            # for NLE
            while len(stk_nle) > 0 and stk_nle[-1] > A[i]:
                top_i = stk_nle[-2]
                stk_nle.pop()
                stk_nle.pop()
                rht[top_i] = i - top_i
            stk_nle.append(i)
            stk_nle.append(A[i])

        # print(lft)
        # print(rht)

        mod = 1e9 + 7
        ans = 0
        for i in range(len(A)):
            ans += A[i] * lft[i] * rht[i]
        ans = ans % mod
        return int(ans)