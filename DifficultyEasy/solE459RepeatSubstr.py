"""
    from DifficultyEasy.solE459RepeatSubstr import Solution
    s = "abab"
    s = "abcabc"
    # s = "aba"
    print(s)
    ans = Solution().repeatedSubstringPattern(s)
    print("Repeated substr? {}".format(ans))
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # return self.firstImpl(s)

        l = int(len(s) / 2)
        while l > 0:
            if len(s) % l != 0:
                continue
            count = len(s) / l
            if s[:l] * count == s:
                return True
            l -= 1

        return False



    def firstImpl(self, s):
        len_whole = len(s)

        if len_whole <= 1:
            return False

        # from single character to "len(s) - 1" string
        for len_sub in range(int(len_whole / 2), 0, -1):

            if len_whole % len_sub != 0:
                continue

            num_of_subs = len_whole / len_sub

            cnt = 0
            for j in range(1, num_of_subs):
                if s[len_sub*j:len_sub*(j+1)] != s[:len_sub]:
                    break
                cnt += 1

            if cnt == num_of_subs - 1:
                return True

        return False