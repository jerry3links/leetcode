"""
    from DifficultyHard.solH065ValidNumber import Solution
    s = "-90e3"
    s = "0.1"
    s = "53.5e93"
    print(s)
    ans = Solution().isNumber(s)
    print("ans: {}".format(ans))
"""


class Solution(object):

    c2i = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # print("len(s): {}".format(len(s)))
        if len(s) == 0:
            return False


        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        sign = None
        if i < len(s) and s[i] == '-':
            sign = i
            i += 1
        elif i < len(s) and s[i] == '+':
            sign = i
            i += 1

        if i == len(s):
            return False

        # print("sign: {}".format(sign))

        while i < len(s) and s[i] in self.c2i.keys():
            i += 1

        # print("sign: {}, i: {}".format(sign, i))

        if i - 1 == sign:
            return False

        # print("i: {}".format(i))

        dot = None
        exp = None
        if i < len(s) and s[i] == '.':
            # print("DOT")
            dot = i
            i += 1
        elif i < len(s) and s[i] == 'e':
            # print("EXP")
            exp = i
            i += 1



        while i < len(s) and s[i] in self.c2i.keys():
            i += 1

        if exp:
            # print("exp: {}".format(exp))
            if i < len(s) and s[i] == '.':
                dot = i
                i += 1
        elif dot:
            # print("dot: {}".format(dot))
            if i < len(s) and s[i] == 'e':
                exp = i
                i += 1

        while i < len(s) and s[i] in self.c2i.keys():
            i += 1

        dom = None
        if exp > dot:
            dom = 'e'
        elif exp < dot:
            dom = '.'

        # print("dom: {}".format(dom))
        #
        if not dom:
            while i < len(s) and s[i] == ' ':
                i += 1
            if i == len(s):
                return True
            else:
                return False
        elif dom == 'e':
            # print("E")
            while i < len(s) and s[i] in self.c2i.keys():
                i += 1
        else:
            # print("D")
            while i < len(s) and s[i] in self.c2i.keys():
                i += 1
            # print("dot: {}, i : {}".format(dot, i))
            if i < len(s) and s[i] == 'e':
                exp = i
                i += 1
            while i < len(s) and s[i] in self.c2i.keys():
                i += 1
            if i - 1 == exp:
                return False

        # print("i: {}".format(i))
        while i < len(s) and s[i] == ' ':
            i += 1

        if i == len(s):
            return True
        else:
            return False