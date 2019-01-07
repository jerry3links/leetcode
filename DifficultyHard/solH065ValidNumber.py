"""
    from DifficultyHard.solH065ValidNumber import Solution

    s_map = {
                "-90e3": True
                , "0": True
                , "+23e-123.132132123": False
                , "23.123e132132123": True
                , "23.e132132123": True,
                "0.1": True,
                ".1": True
                , "   0123e12.12e123": False
                , "2e0": True
                , ".0e": False
                , "46.e3": True
                , "32.e-80123": True
                , "53.5e93": True
                , "  + ": False
                , "0.   ": True
                , "   ": False
    }

    cnt = 0
    for k in s_map:
        try:
            assert Solution().isNumber(k) == s_map[k]
            # print("[{}]=>{}".format(k, Solution().isNumber(k)))
            cnt += 1
        except AssertionError:
            print("[{}] should be {}, cnt: {}".format(k, s_map[k], cnt))

    if cnt == len(s_map):
        print("All pass!")
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
        return self.firstImpl(s)

    def firstImpl(self, s):
        i = 0
        # leading whitespaces
        while i < len(s) and s[i] == self.space:
            i += 1

        # sign
        if i < len(s) and s[i] in self.signs:
            i += 1

        # digit
        digits_before_shed = 0
        while i < len(s) and s[i] in self.c2i.keys():
            i += 1
            digits_before_shed += 1

        # decimal point or exponential
        exp = dec = None
        if i < len(s):
            if s[i] == self.decpt:
                dec = i
                i += 1
            elif s[i] == self.expon:
                if digits_before_shed == 0:
                    return False
                exp = i
                i += 1

        # begin with exponential
        # signs are allowed, but if there are no digits then return False
        if exp is not None:
            if i < len(s) and s[i] in self.signs:
                i += 1

            digits_after_exp = 0
            while i < len(s) and s[i] in self.c2i.keys():
                i += 1
                digits_after_exp += 1

            if digits_after_exp == 0:
                return False

        # deal with the part after decimal point
        digits_after_decimal = 0
        if dec is not None:

            while i < len(s) and s[i] in self.c2i.keys():
                i += 1
                digits_after_decimal += 1

            if i < len(s) and s[i] == self.expon:
                exp = i
                i += 1

            if exp is not None:
                if i < len(s) and s[i] in self.signs:
                    i += 1

            digits_after_exp = 0
            while i < len(s) and s[i] in self.c2i.keys():
                i += 1
                digits_after_exp += 1

            if exp is not None and digits_after_exp == 0:
                return False

        while i < len(s) and s[i] == self.space:
            i += 1

        if i >= len(s) and ((exp is not None and digits_before_shed > 0) or
                            (dec is not None and
                             (digits_after_decimal > 0 or digits_before_shed > 0)) or
                            (dec is None and exp is None and digits_before_shed > 0)):
            return True
        else:
            return False

    def algorithmeticByChar(self, s):
        # todo leading and lagging spaces
        s = s.strip()
        # print(s)
        if len(s) == 0: return False

        # keep track of e, -, +, ., and the presence of numbers
        hasE = hasN = hasP = hasD = numberEncountered = numberAfterE = False
        prev = None  # keep track of previous letter
        # print(["[" + str(i) + "]" + str(l) for i, l in enumerate(s)])
        for i, l in enumerate(s):
            if l == 'e':
                if not numberEncountered: return False  # can't start with e
                if hasE: return False  # only one e permited
                hasE = True
                hasN = False  # reset negative sign switch to allow another -
                hasP = False  # reset positive sign switch to allow another
            elif l == '-':
                if hasN: return False  # only one permited unless reset by e
                if not (i == 0 or prev == 'e'): return False  # must start the number
                hasN = True
            elif l == '+':
                if hasP: return False  # only one permited unless reset by e
                if not (i == 0 or prev == 'e'): return False  # must start the number
                hasP = True
            elif l == '.':
                if hasD: return False  # only one permited
                if hasE: return False  # no decimals after e
                hasD = True
            elif 48 <= ord(l) <= 57:
                numberEncountered = True
                if hasE: numberAfterE = True
            else:
                return False

            prev = l

        if not numberEncountered: return False  # if no numbers it's not a number

        if hasE:
            if hasE and not numberAfterE: return False  # e needs number after it

        return True