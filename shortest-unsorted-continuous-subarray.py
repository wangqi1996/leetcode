class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _len, current_max, index = len(nums), nums[0], 1
        while index < _len:
            if nums[index] < current_max:
                break
            current_max, index = nums[index], index + 1
        if index == _len:
            return 0
        _min, _max, start, index, end = nums[index], nums[index], index, index + 1, index
        while index < _len:
            if nums[index] < current_max:
                end = index
            current_max = max(current_max, nums[index])
            index += 1
        _min, _max, index = nums[start], nums[end], start
        while index <= end:
            _max = max(nums[index], _max)
            _min = min(nums[index], _min)
            index += 1
        index = start - 1
        while index >= 0 and nums[index] > _min:
            _max = max(nums[index], _max)
            index -= 1
        index1 = index + 1
        index = end + 1
        while index < _len and nums[index] < _max:
            _max = max(nums[index], _max)
        return max(index - index1, 0)


if __name__ == '__main__':
    print(Solution().findUnsortedSubarray([2]))
