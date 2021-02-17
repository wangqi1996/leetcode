class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 1:
            return nums
        current_index, current_max, result = 0, nums[0], []
        _len = len(nums)
        for i in range(0, _len):
            if i < k - 1:
                if nums[i] >= current_max:
                    current_max, current_index = nums[i], i
                continue
            if nums[i] >= current_max:
                current_max, current_index = nums[i], i

            if (i - k) >= current_index:
                current_max, current_index = nums[i - k + 1], i - k + 1
                for j in range(i - k + 2, i + 1):
                    if nums[j] >= current_max:
                        current_max, current_index = nums[j], j
            result.append(current_max)
        return result


if __name__ == '__main__':
    print(Solution().maxSlidingWindow([7, 2, 4], 2))
