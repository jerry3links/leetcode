"""
    from DifficultyMedium.solM006ZigZagConv import Solution
    # s = "PAYPALISHIRING"; numRows = 3
    s = "PAYPALISHIRINGXYZ"; numRows = 4
    # s = "A"; numRows = 1
    # s = "AB"; numRows = 1
    print("s: {}, numRows: {}".format(s, numRows))
    ans = Solution().convert(s, numRows)
    print(ans)
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if len(s) <= 0 or numRows <= 0:
            return ""

        if len(s) == 1 or numRows == 1:
            return s

        zz = [[] for _ in range(numRows)]
        i = 0
        while i < len(s):

            head = s[i:i+numRows]
            tail = s[i+numRows:i+(2*numRows)-2]

            # processing head
            for j, c in zip(range(numRows), head):
                zz[j].append(c)

            # processing tail
            if len(tail) > 0:
                zz[numRows - 1] += ["" for _ in range(numRows - 2)]
                for j in range(len(tail)):
                    s_head = ["" for _ in range(0, j)]
                    s_tail = ["" for _ in range(j + 1, numRows - 2)]
                    zz[numRows - j - 2] += s_head + list(tail[j]) + s_tail
                zz[0] += ["" for _ in range(numRows - 2)]

            i += 2 * numRows - 2

        ans = "".join(["".join(row) for row in zz])

        return ans
