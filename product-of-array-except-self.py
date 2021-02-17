class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        _len = len(nums)
        if _len < 2:
            return [] if _len == 0 else [1]
        result = [1 for _ in range(_len)]
        for i in range(1, _len):
            result[i] = result[i - 1] * nums[i - 1]
        n = nums[-1]
        for i in range(_len - 2, -1, -1):
            result[i] *= n
            n *= nums[i]
        return result


if __name__ == '__main__':
    print(Solution().productExceptSelf([]))
