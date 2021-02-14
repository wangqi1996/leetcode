class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return nums
        _max = nums[0]
        _min = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for n in nums[1:]:
            pre1 = pre_max * n
            pre2 = pre_min * n
            pre_max = max(pre1, pre2, n)
            pre_min = min(pre1, pre2, n)
            _max = max(_max, pre_max)
            _min = min(_min, pre_min)

        return _max


if __name__ == '__main__':
    print(Solution().maxProduct([3, -1, 4]) == 4)
    print(Solution().maxProduct([2, 3, -2, 4]) == 6)
    print(Solution().maxProduct([-2, 0, -1]) == 0)
    print(Solution().maxProduct([1, 1, 1]) == 1)
    print(Solution().maxProduct([1, 2, 1]) == 2)
    print(Solution().maxProduct([-1, -2, 1]) == 2)
