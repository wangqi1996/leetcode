class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        _len = len(nums)
        if _len < 2:
            return max(nums)
        dp = [0 for _ in range(_len)]
        dp[0] = nums[0]
        dp[1] = nums[1]
        _max = dp[0]
        for j in range(2, _len):
            dp[j] = _max + nums[j]
            _max = max(_max, dp[j - 1])
        return max(_max, dp[_len - 1])


if __name__ == '__main__':
    print(Solution().rob([1, 2, 3, 1]))
