class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        _len = len(nums)
        if _len == 0:
            return [-1, -1]
        left, right = 0, _len - 1
        if nums[0] != target:
            start = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid - 1] != target and nums[mid] == target:
                    start = mid
                    break
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        else:
            start = 0

        if start == -1:
            return [-1, -1]
        right = _len - 1
        if nums[-1] != target:
            end = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target and nums[mid + 1] != target:
                    end = mid
                    break
                elif nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
        else:
            end = _len - 1

        return [start, end]


if __name__ == '__main__':
    print(Solution().searchRange([7, 8], 7) == [0, 0])
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 7) == [1, 2])
    print(Solution().searchRange([7, 7, 7, 8, 8, 10], 7) == [0, 2])
    print(Solution().searchRange([5, 7, 7, 8, 8, 8], 8) == [3, 5])
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 17) == [-1, -1])
    print(Solution().searchRange([7, 7], 7) == [0, 1])
    print(Solution().searchRange([], 7) == [-1, -1])
    print(Solution().searchRange([7], 7) == [0, 0])
    print(Solution().searchRange([7], 8) == [-1, -1])
