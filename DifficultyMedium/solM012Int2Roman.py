"""
    from DifficultyMedium.solM012Int2Roman import Solution

    benches = {
                3: "III"
                , 4: "IV"
                , 9: "IX"
                , 10: "X"
                , 58: "LVIII" ,
                1994: "MCMXCIV"
    }

    cnt = 0
    for val in benches:
        try:
            assert Solution().intToRoman(val) == benches[val]
            cnt += 1
        except AssertionError:
            print("[{}] should be {}, cnt: [{}]".format(val, benches[val], cnt))

    if cnt == len(benches):
        print("All pass!")
"""

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution(object):
    ixc = {
        "I": ("V", "X"),
        "X": ("L", "C"),
        "C": ("D", "M"),
        "M": None
    }

    chs = "IXCM"


    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        RULE = {
            "I": ("V", "X"),
            "X": ("L", "C"),
            "C": ("D", "M"),
            "M": None
        }

        BASE = "IXCM"

        cnt = 0
        res = ""

        while num > 0 and cnt < len(BASE):
            num, r = divmod(num, 10)

            base = BASE[cnt]
            pair = RULE[base]
            if 0 < r <= 4:
                tmp = base
                if r == 4 and pair:
                    tmp += pair[0]
                else:
                    for _ in range(1, r):
                        tmp += base
                res = tmp + res
            elif 5 <= r < 9 and pair:
                tmp = pair[0]
                if 5 < r < 9:
                    for _ in range(r % 5):
                        tmp += base
                res = tmp + res
            elif r == 9 and pair:
                res = base + pair[1] + res

            cnt += 1

        return res

    # python
    # Runtime: 72 ms, faster than 80.00%
    # Memory Usage: 10.6 MB, less than 100.00%
    def secondImpl(self, num):
        # print("PROCESSING [{}] ...".format(num))
        cnt = 0
        rst = ""

        while num > 0 and cnt < len(self.chs):
            num, r = divmod(num, 10)
            # print("cnt: {}, num: {}, r: {}".format(cnt, num, r))

            base = self.chs[cnt]
            pair = self.ixc[base]
            if 0 < r <= 4:
                tmp = base
                if r == 4 and pair:
                    tmp += pair[0]
                else:
                    for _ in range(1, r):
                        tmp += base
                rst = tmp + rst
            elif 5 <= r < 9 and pair:
                tmp = pair[0]
                if 5 < r < 9:
                    for _ in range(r % 5):
                        tmp += base
                rst = tmp + rst
            elif r == 9 and pair:
                rst = base + pair[1] + rst

            cnt += 1

        return rst

    def firstImpl(self, num):
        # print("PROCESSING [{}] ...".format(num))
        cnt = 0
        rst = ""
        while num > 0:
            num, r = divmod(num, 10)
            # print("cnt: {}, r: {}".format(cnt, r))

            # 1
            if cnt == 0:
                if 0 < r < 4:
                    for _ in range(r):
                        rst += "I"
                elif r == 4:
                    rst += "IV"
                elif 5 <= r < 9:
                    rst += "V"
                    if 5 < r < 9:
                        for _ in range(r % 5):
                            rst += "I"
                elif r == 9:
                    rst += "IX"
            # 10
            elif cnt == 1:
                if 0 < r < 4:
                    for _ in range(r):
                        rst = "X" + rst
                elif r == 4:
                    rst = "XL" + rst
                elif 5 <= r < 9:
                    tmp = "L"
                    if 5 < r < 9:
                        for _ in range(r % 5):
                            tmp += "X"
                    rst = tmp + rst
                elif r == 9:
                    rst = "XC" + rst

            # 100
            elif cnt == 2:
                if 0 < r < 4:
                    for _ in range(r):
                        rst = "C" + rst
                elif r == 4:
                    rst = "CD" + rst
                elif  5 <= r < 9:
                    tmp = "D"
                    if 5 < r < 9:
                        for _ in range(r % 5):
                            tmp += "C"
                    rst = tmp + rst
                elif r == 9:
                    rst = "CM" + rst

            elif cnt == 3:
                if 0 < r < 4:
                    for _ in range(r):
                        rst = "M" + rst
                else:
                    break


            cnt += 1
        # print(rst)
        return rst