class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [100000 for _ in range(n + 1)]
        import math
        _len = int(math.sqrt(n)) + 1
        square_num = [i * i for i in range(1, _len)]
        for i in range(1, n + 1):
            if i in square_num:
                dp[i] = 1
                continue
            for j in square_num:
                if j > i:
                    break
                dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().numSquares(30))
