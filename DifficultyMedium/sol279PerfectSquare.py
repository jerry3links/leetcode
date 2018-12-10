"""Put the following in main of demo,py
from DifficultyMedium.sol103ZigZagBTree import Solution
n_lst = [0, 1, 12, 13]
for n in n_lst:
    print("n: {}".format(n))
    a = Solution().numSquares(n)
    print("num of ps: {}".format(a))
"""


class Solution:
    def numSquares(self, n):
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1

        print(lst)

        cnt = 0
        toCheck = {n}

        while toCheck:
            print(len(toCheck))
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt