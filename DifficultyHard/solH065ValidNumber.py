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

    space = ' '

    signs = {'+', '-'}

    decpt = '.'

    expon = 'e'

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        i = 0
        # leading whitespaces
        while i < len(s) and s[i] == self.space:
            i += 1

        # sign
        signed = 0
        if i < len(s) and s[i] in self.signs:
            signed = i
            i += 1

        # print("signed before [{}]".format(i))

        # digit
        digits_before_shed = 0
        while i < len(s) and s[i] in self.c2i.keys():
            i += 1
            digits_before_shed += 1
        # print("digits_before_shed: {}".format(digits_before_shed))

        # print("first digit-part ends before [{}]".format(i))

        # decimal point or exponential
        shed = None
        if i < len(s):
            if s[i] == self.decpt:
                shed = (self.decpt, i)
                i += 1
            elif s[i] == self.expon:
                if digits_before_shed == 0:
                    return False
                shed = (self.expon, i)
                i += 1

        # begin with exponential
        if shed and shed[0] == self.expon:

            # print("currently at [{}], shed at [{}]".format(i, shed[1]))
            # if shed[1] - 1 == signed:
            #     return False

            if i < len(s) and s[i] in self.signs:
                signed = i
                i += 1

            while i < len(s) and s[i] in self.c2i.keys():
                i += 1
            # print("digits after exp ends before [{}]".format(i))
            if i <= shed[1] + 1 or i <= signed + 1:
                return False

        # deal with the part after decimal point
        digits_after_decimal = 0
        if shed and shed[0] == self.decpt:

            while i < len(s) and s[i] in self.c2i.keys():
                i += 1
                digits_after_decimal += 1
            print("digits_after_decimal: {}".format(digits_after_decimal))

            print("digits after dot ends before [{}]".format(i))

            exp = None
            if i < len(s) and s[i] == self.expon:
                exp = i
                i += 1

            # if exp and (exp - 1 == shed[1]):
            #     return False
            signed = None
            if exp:
                if i < len(s) and s[i] in self.signs:
                    signed = i
                    i += 1


            digits_after_exp = 0
            while i < len(s) and s[i] in self.c2i.keys():
                i += 1
                digits_after_exp += 1
            if exp and digits_after_exp == 0:
                return False


        print("currently at {}".format(i))
        while i < len(s) and s[i] == self.space:
            i += 1

        if i == len(s) and ((shed and digits_before_shed > 0) or
                            (shed and digits_after_decimal > 0) or
                            (not shed and digits_before_shed > 0)):
            return True
        else:
            return False

