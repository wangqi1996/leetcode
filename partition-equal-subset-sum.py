class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        _sum //= 2
        dp = [False for _ in range(_sum + 1)]
        dp[0] = True
        for n in nums:
            for i in range(_sum, n - 1, -1):
                dp[i] |= dp[i - n]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().canPartition([1, 5, 11, 5]))
