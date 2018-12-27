"""
    from StringArray.sol028StrStr import Solution
    haystack = "hello"; needle = "ll"
    print("haystack: {}, needle: {}".format(haystack, needle))
    ans = Solution().strStr(haystack, needle)
    print("ans: {}".format(ans))
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(needle) == 0:
            return 0

        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)+1):
            for j in range(len(needle)+1):
                if j == len(needle):
                    return i
                if j + i == len(haystack):
                    return -1
                if haystack[i+j] != needle[j]:
                    break

        return -1





