"""
    from Rethink.solM006ZZConvRe import Solution
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

        if numRows == 1:
            return s

        zz = ["" for _ in range(numRows)]
        i = 0
        while i < len(s):

            # processing head
            for j in range(numRows):
                if i < len(s):
                    zz[j] += s[i]
                    i += 1

            # processing tail
            for j in range(numRows - 2):
                if i < len(s):
                    zz[numRows - j - 2] += s[i]
                    i += 1

        ans = "".join(zz)

        return ans


        # if numRows == 1:
        #     return s
        #
        # direction = 1  # to control row# movement
        # rowIndex = 0  # indicate which lane to add element
        # result = ['' for _ in range(numRows)]  # declare a nested list in which each row is a list
        #
        # for i in range(len(s)):
        #     result[rowIndex] += (s[i])
        #     rowIndex += direction
        #     if rowIndex == 0 or rowIndex == numRows - 1:
        #         direction *= -1
        # return ''.join(result)

        # if len(s) <= numRows:
        #     return s
        # rows = self.zigzag(s, numRows)
        # answer = "".join(rows)
        # return answer

    def zigzag(self, s, numRows):
        rows = ["" for _ in range(numRows)]
        i = 0
        while i < len(s):
            for r in range(numRows):
                if i < len(s):
                    rows[r] += s[i]
                    i += 1
            if numRows > 2:
                for m in range(numRows - 2, 0, -1):
                    if i < len(s):
                        rows[m] += s[i]
                        i += 1
        return rows
