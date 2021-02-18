class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        _len = len(prices)
        if _len <= 1:
            return 0
        dp = [[0, 0, 0] for _ in range(_len)]  # 持有 卖出 不持有
        dp[0][0] = -prices[0]
        for i in range(1, _len):
            dp[i][-1] = max(dp[i - 1][-1], dp[i - 1][1])  # 不持有
            dp[i][1] = dp[i - 1][0] + prices[i]  # 卖出
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][-1] - prices[i])  # 持有
        return max(dp[-1][1], dp[-1][-1])


if __name__ == '__main__':
    print(Solution().maxProfit([1, 2, 3, 0, 2]))
