class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        current_sum = nums[0]
        for n in nums[1:]:
            if current_sum >= 0:
                current_sum += n
            else:
                current_sum = n
            max_sum = max(max_sum, current_sum)
        return max_sum


if __name__ == '__main__':
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
