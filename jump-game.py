class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _len = len(nums)
        if _len <= 1:
            return True
        max_len = 0
        for i in range(_len - 1):
            if i > max_len:
                return False
            max_len = max(max_len, i + nums[i])
            if max_len >= _len - 1:
                return True
        return False


if __name__ == '__main__':
    print(Solution().canJump([2, 3, 1, 1, 4]))
    print(Solution().canJump([3, 2, 1, 0, 4]))
