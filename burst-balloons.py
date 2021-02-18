class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _len = len(nums)
        if _len == 0:
            return 0
        nums = [1] + nums + [1]
        _len = _len + 2
        dp = [[0 for _ in range(_len)] for _ in range(_len)]
        for i in range(2, _len):
            for s in range(0, _len - i):
                e = s + i
                n = nums[s] * nums[e]
                for k in range(s + 1, e):
                    dp[s][e] = max(dp[s][e], n * nums[k] + dp[s][k] + dp[k][e])
        return dp[0][_len - 1]


if __name__ == '__main__':
    print(Solution().maxCoins([3, 1, 5, 8]))
    print(Solution().maxCoins([3, 2]))
    print(Solution().maxCoins([3]))
