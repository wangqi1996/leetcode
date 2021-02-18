class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _len = len(nums)
        dp = [1 for _ in range(_len)]
        for i in range(_len):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    print(Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
