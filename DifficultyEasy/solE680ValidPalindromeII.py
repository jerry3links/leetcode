"""
    from DifficultyEasy.solE680ValidPalindromeII import Solution
    s = "abca"
    print(s)
    ans = Solution().validPalindrome(s)
    print("ans: {}".format(ans))
"""


class Solution(object):

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True

        def isPalindrome(s):
            # s[::-1] is reversed s
            if s[::-1] == s:
                return True
            return False

        if isPalindrome(s):
            return True

        h = 0
        t = len(s) - 1

        while h < t:

            if s[h] != s[t]:
                return isPalindrome(s[h+1:t+1]) or isPalindrome(s[h:t])

            h += 1
            t -= 1

        return True


