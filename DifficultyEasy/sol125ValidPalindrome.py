"""

    from DifficultyEasy.sol125ValidPalindrome import Solution

    s = "A man, a plan, a canal: Panama"
    # "A man, a plan, a canal: Panam"
    print("{}".format(s))
    ans = Solution().isPalindrome(s)
    print("ans: {}".format(ans))

"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        len_str = len(s)

        if len_str <= 1:
            return True

        str_new = s.lower()
        str_new = "".join([c if c.isalnum() else "" for c in str_new])
        # print(str_new)
        len_new = len(str_new)

        # for i in range(len(str_new)):
        #     print("{}: {}".format(i, str_new[i]))

        i = 0
        m = int(len_new / 2)
        # print(m)
        while i < m:
            if str_new[i] == str_new[len_new - i - 1]:
                i += 1
                continue
            else:
                break

        if i == m:
            return True

        return False
