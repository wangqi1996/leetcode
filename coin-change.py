class Solution(object):
    def coinChange(self, coins: list, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        _len = len(coins)
        dp = [10000 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
                continue
            for j in coins:
                dp[i] = min(dp[i - j] + 1, dp[i]) if i - j >= 0 else dp[i]
        return dp[-1] if dp[-1] < 10000 else -1


if __name__ == '__main__':
    print(Solution().coinChange([312343256], 2))
