"""
    from DifficultyMedium.sol322CoinChangeDP import Solution
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

        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0
        coins.sort()

        for coin in coins:
            # print("for coin {}".format(coin))
            # s = ""
            for i in range(coin, amount + 1):
                # s += str(i) + " "
                # print("i =  {}, amount - i = {}".format(i, amount - i))
                dp[i] = min(dp[i], dp[i - coin] + 1)
            # print(s)
        # print(dp)

        best = dp[-1]

        if best == float("inf"):
            return -1

        return best

