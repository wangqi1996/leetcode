class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if S > 1000:
            return 0
        _len = len(nums)
        dp = [[0 for _ in range(_len)] for _ in range(2002)]
        pre = [nums[0] + 1000, 1000 - nums[0]]
        for p in pre:
            dp[p][0] = 1
        for j, n in enumerate(nums[1:]):
            new = []
            for p in pre:
                new.extend([p + n, p - n])
                dp[p + n][j + 1] += dp[p][j]
                dp[p - n][j + 1] += dp[p][j]
            pre = set(new)
        return dp[S + 1000][_len - 1]


if __name__ == '__main__':
    print(Solution().findTargetSumWays(
        [43, 9, 26, 24, 39, 40, 20, 11, 18, 13, 14, 30, 48, 47, 37, 24, 32, 32, 2, 26],
        47))
