"""
    # Input: [3,1,2,4]
    # Output: 17
    # Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]

    from DifficultyMedium.sol907SumOfSubArrMin import Solution
    A = [3,1,2,4]
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

        # create sub-array
        sum_of_min = 0
        for i in range(0, len(A)):
            length = i + 1
            # print("for length {}".format(length))
            # s = ""
            for j in range(len(A) - i):
                # s += str(j) + " "
                sub_array = A[j:j+length]
                # print(sub_array)
                sum_of_min += min(sub_array)
                # all_array.append(sub_array)
            # print(all_array)

        return sum_of_min