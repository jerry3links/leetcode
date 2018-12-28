"""
    from StringArray.sol151MReverseWords import Solution
    s = "the sky is blue"
    print(s)
    ans = Solution().reverseWords(s)
    print("ans: {}".format(ans))
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        a = s.split(" ")
        # print(len(a))
        # print(a)
        b = [a[i] for i in range(len(a) - 1, -1, -1) if a[i] != ""]
        # print(b)
        res = " ".join(b)
        # print(res)
        return res
