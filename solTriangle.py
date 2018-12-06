"""Put the following in main of demo,py
from solTriangle import Solution
lst = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
a = Solution().minimumTotal(lst)
print("min path: {}".format(a))
"""


class Solution:
    def minimumTotal(self, trg):

        last_len = len(trg[-1])

        if last_len <= 0:
            return -1

        depths = len(trg)

        for i in range(len(trg)):
            zeros = [0 for j in range(last_len - i - 1)]
            trg[i] += zeros

        for i in range(depths - 2, -1, -1):

            for j in range(last_len - 1):

                if trg[i+1][j] < trg[i+1][j+1]:
                    trg[i][j] += trg[i+1][j]
                else:
                    trg[i][j] += trg[i+1][j+1]

        return trg[0][0]