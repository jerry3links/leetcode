"""
    from StringArray.solM003LongestSubstr import Solution
    # s = "abcabcbb"
    # s = "aab"
    # s = "dvdf"
    # s = "bbbbbb"
    # s = "abcde"
    s = "pwwkew"
    print(s)
    ans = Solution().lengthOfLongestSubstring(s)
    print(ans)
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.thirdImpl(s)

    def thirdImpl(self, s):
        if len(s) == 0:
            return 0

        exist = {}
        for v in set(s):
            exist[v] = False

        max_len = 0
        head = 0
        for tail in range(len(s)):
            while exist[s[tail]]:
                exist[s[head]] = False
                head += 1
            exist[s[tail]] = True
            max_len = max(max_len, tail - head + 1)
            if max_len == len(s):
                break

        return max_len

    def templateImpl(self, s):
        if len(s) == 0:
            return 0

        exist = [False for _ in range(256)]

        i = 0
        maxLen = 0
        for j in range(len(s)):
            while exist[ord(s[j])]:
                exist[ord(s[i])] = False
                i += 1
            exist[ord(s[j])] = True
            maxLen = max(maxLen, j - i + 1)

        return maxLen

    def secondImpl(self, s):
        if len(s) == 0:
            return 0

        max_len = 0
        i = 0
        while i < len(s):
            basket = {s[i]: i}
            reset = False
            for j in range(i + 1, len(s)):
                if s[j] in basket:
                    i = basket[s[j]] + 1
                    reset = True
                    break
                basket[s[j]] = j

            if len(basket) > max_len:
                max_len = len(basket)

            if not reset:
                break

        return max_len

    def firstImpl(self, s):
        if len(s) == 0:
            return 0

        l = list(s)

        max_len = 0
        for i in range(len(l)):
            basket = {l[i]}
            for j in range(len(l[:i])-1, -1, -1):
                if l[j] in basket:
                    break
                basket.add(l[j])

            if len(basket) > max_len:
                max_len = len(basket)

        return max_len

