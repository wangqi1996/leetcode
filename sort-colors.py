class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        point_0 = 0
        _len = len(nums)
        point_2 = len(nums) - 1
        point_1 = 0
        while point_1 <= point_2:
            while point_1 < _len and nums[point_1] == 1:
                point_1 += 1
            if point_1 > point_2:
                return nums
            if nums[point_1] == 0:
                if point_1 != point_0:
                    nums[point_0], nums[point_1] = 0, 1
                    point_1 += 1
                else:
                    nums[point_0] = 0
                point_0 += 1
                point_1 = max(point_1, point_0)
            elif nums[point_1] == 2:
                nums[point_2], nums[point_1] = 2, nums[point_2]
                point_2 -= 1
                while point_2 >= 0 and nums[point_2] == 2:
                    point_2 -= 1

        return nums


if __name__ == '__main__':
    print(Solution().sortColors([2, 0, 2, 1, 1, 0]))
    print(Solution().sortColors([2, 1, 2, 1, 1, 1]))
    print(Solution().sortColors([1, 1, 1, 1, 1, 1]))
    print(Solution().sortColors([0, 0, 0, 0, 0, 0]))
    print(Solution().sortColors([0]))
