"""
    from DifficultyEasy.solE709ToLowercase import Solution
    input = "Hello"
    print("input: {}".format(input))
    ans = Solution().toLowerCase(input)
    print("output: {}".format(ans))
"""

# A-Z = 65-90
# a-z = 97-122

class Solution(object):
    def toLowerCase(self, input):
        """
        :type str: str
        :rtype: str
        """

        if len(input) < 1:
            return None

        s = bytearray(input, encoding='ascii')

        for i in range(len(input)):

            if 65 <= ord(input[i]) <= 90:
                s[i] = chr(ord(input[i])+32)


        return s

    # Runtime: 20 ms, faster than 81.71% of Python online submissions for To Lower Case.
    # Memory Usage: 10.9 MB, less than 8.49% of Python online submissions for To Lower Case.
    def firstImp(self, input):
        if len(input) < 1:
            return None

        res = ""

        for i in range(len(input)):

            if 65 <= ord(input[i]) <= 90:
                res += chr(ord(input[i])+32)
            elif 97 <= ord(input[i]) <= 122:
                res += input[i]
            else:
                res += input[i]

        return res