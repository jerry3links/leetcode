"""
    from DifficultyMedium.sol322CoinChange import Solution
    coins = [1,2,5]; amount = 3
    ans = Solution().coinChange(coins, amount)
    print("coins = {}; amount = {}".format(coins, amount))
    print("ans = {}".format(ans))
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # beware of [1] and 0
        if amount == 0:
            return 0

        coins.sort()

        Q = [(amount, 1)]
        # if done, do not put into queue again
        done = set()

        while Q:
            remain, level = Q.pop(0)
            for i in coins:
                if remain == i:
                    return level
                elif remain < i:
                    break
                elif remain - i not in done:
                    Q.append((remain - i, level + 1))
                    done.add(remain - i)

        return -1

