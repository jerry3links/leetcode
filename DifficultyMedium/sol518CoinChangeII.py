"""
    from DifficultyMedium.sol518CoinChangeII import Solution
    amount = 5
    coins = [1,2,5]
    ans = Solution().change(amount, coins)
    print(ans)
"""

# Note: all possible combinations (# of combinations)
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount < 1:
            return 1

        if not coins:
            return 0

        coins.sort()

        f = [[0]*(amount+1) for _ in range(len(coins))]
        for j in range(1, amount+1):
            if j % coins[0] == 0:
                f[0][j] = 1
        for i in range(len(coins)):
            f[i][0] = 1

        for i in range(1,len(coins)):
            for target in range(1, amount + 1):
                if target >= coins[i]:
                    f[i][target] = f[i-1][target] + f[i][target - coins[i]]
                else:
                    f[i][target] = f[i-1][target]

        return f[-1][-1]
