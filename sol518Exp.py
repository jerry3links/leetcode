"""
    from sol518Exp import Solution
    amount = 5
    coins = [1,2,5]
    ans = Solution().change(amount, coins)
    print(ans)
"""


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount < 1:
            return 0
        candidates = [v for v in coins if v <= amount]
        if len(candidates) < 1:
            return 0

        toCheck = {amount}

        print("candidates: {}".format(candidates))

        visited = {}

        # cnt = 1
        while toCheck:
            # cnt += 1
            temp = set()
            ans = 0
            for x in toCheck:
                # print("amount to check: {}, Q: {}".format(x, toCheck))
                print("TARGET: {}".format(x))
                if x not in visited:
                    visited[x] = 0
                for y in candidates:
                    if x == y:
                        print(" use ${}, remain: {}, got one way! {}".format(y, x - y, toCheck))
                        cnt = 0
                        for v in toCheck:
                            if v in candidates:
                                cnt += 1
                        if cnt == len(toCheck):
                            ans += 1
                        visited[x] += 1
                        # print("Got one way to makeup! cnt: {}".format(cnt))
                    elif x < y:
                        break
                    else:
                        temp.add(x-y)
                        print(" use ${}, remain: {}, add to temp: {}".format(y, x - y, temp))
            toCheck = temp
        # print(visited)


        return ans