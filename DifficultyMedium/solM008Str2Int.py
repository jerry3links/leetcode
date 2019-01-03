"""
    from DifficultyMedium.solM008Str2Int import Solution
    s = "42"
    s = "words and 987"
    s = "   +0 123"
    print(s)
    ans = Solution().myAtoi(s)
    print("ans: {}".format(ans))
"""


class Solution(object):

    BOUND_UP = 2 ** 31 - 1
    BOUND_BT = 2 ** 31

    c2i = {
        '0': 0, '1': 1, '2': 2,
        '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8,
        '9': 9
    }

    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """

        # return self.selfImp(s)

        i = 0
        while i < len(s) and s[i] == ' ':
            i+=1
        sign = 1
        if i < len(s) and s[i] == '+':
            i += 1
        elif i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        ans = 0
        while i < len(s) and s[i] in self.c2i.keys():
            digit = self.c2i[s[i]]
            ans = ans * 10 + digit
            if sign == 1 and ans > self.BOUND_UP:
                return self.BOUND_UP
            elif sign == -1 and ans > self.BOUND_BT:
                return self.BOUND_BT * -1
            i+=1

        return ans * sign


    def selfImp(self, s):
        # numericals = [str(v) for v in list(range(10))]
        signs = ['+', '-']
        ans = 0
        signed = None
        for c in list(s):

            if c == ' ' and not signed:
                continue

            if not signed:
                # numericals or chars
                if c not in signs:
                    if c not in self.c2i.keys():
                        break
                    else:
                        signed = 1
                        ans = (ans * 10) + self.c2i[c]
                else: # signs
                    signed = 1 if c == '+' else -1
            else:
                # "   +0  123" will lead us here
                if c not in self.c2i.keys():
                    break
                else:
                    ans = (ans * 10) + self.c2i[c]
                    # if signed == 1 and ans > self.BOUND_UP:
                    #     ans = self.BOUND_UP
                    #     break
                    # elif signed == -1 and ans > self.BOUND_BT:
                    #     ans = self.BOUND_BT
                    #     break

        if signed:
            ans *= signed

        # if ans > self.BOUND_UP:
        #     ans = self.BOUND_UP
        # if ans < (self.BOUND_BT * -1):
        #     ans = (self.BOUND_BT * -1)

        ans = self.BOUND_UP if ans > self.BOUND_UP else ans
        ans = (self.BOUND_BT * -1) if ans < (self.BOUND_BT * -1) else ans

        return ans
