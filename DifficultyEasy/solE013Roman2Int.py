"""
    from DifficultyEasy.solERoman2Int import Solution
    s = "IX"
    s = "MCMXCIV"
    s = "VIII"
    print(s)
    ans = Solution().romanToInt(s)
    print("ans: {}".format(ans))

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

    c2v = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    ixc = {
        "I": ("V", "X"),
        "X": ("L", "C"),
        "C": ("D", "M")
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        self.dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        self.conditions = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}

        slen = len(s)

        i = 0
        nums = []
        while i < slen:
            if s[i] == 'I' or s[i] == 'X' or s[i] == 'C':
                # check next
                if i + 1 < slen:
                    if s[i + 1] in self.conditions[s[i]]:
                        nums.append(self.dic[s[i + 1]] - self.dic[s[i]])
                        i += 2
                        continue

            nums.append(self.dic[s[i]])
            i += 1

        return sum(nums)


        # if len(s) <= 0:
        #     return 0
        #
        # i = 0
        # final_value = 0
        # while i < len(s) - 1:
        #     # print("{} {}".format(s[i], s[i+1]))
        #
        #     if s[i] in self.ixc:
        #         if s[i+1] in self.ixc[s[i]]:
        #             v = self.c2v[s[i+1]] - self.c2v[s[i]]
        #             # print("{}{}: {}".format(s[i], s[i+1], v))
        #             final_value += v
        #             i += 2
        #             continue
        #         else:
        #             v = self.c2v[s[i]]
        #             # print("{}: {}".format(s[i], v))
        #             final_value += v
        #     else:
        #         v = self.c2v[s[i]]
        #         # print("{}: {}".format(s[i], v))
        #         final_value += v
        #     i+=1
        #
        # # print("{} vs {}".format(i, len(s)))
        #
        # if i < len(s):
        #     final_value += self.c2v[s[i]]
        #
        # return final_value
