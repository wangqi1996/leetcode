class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count, i, j, _len = 0, 0, 0, len(nums)
        while i < _len:
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1
        while j < _len:
            nums[j] = 0
            j += 1
        return nums


if __name__ == '__main__':
    print(Solution().moveZeroes([1, 3, 12]))
