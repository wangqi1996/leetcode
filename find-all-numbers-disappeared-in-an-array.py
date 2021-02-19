class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        _len = len(nums)
        for i in range(_len):
            if nums[i] < 0 and nums[-nums[i] - 1] > 0:
                nums[-nums[i] - 1] = -1 * nums[-nums[i] - 1]
            if nums[i] > 0 and nums[nums[i] - 1] > 0:
                nums[nums[i] - 1] *= -1
        result = []
        for i in range(_len):
            if nums[i] > 0:
                result.append(i + 1)
        return result


if __name__ == '__main__':
    print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
