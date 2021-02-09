class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        def process(n1, n2):
            """ insert pos-n2 before pos-n1 and reverse n1-n2"""
            for l in range(n2, n1, -1):
                if nums[l] > nums[n1]:
                    nums[n1], nums[l] = nums[l], nums[n1]
                    break
            reverse(n1 + 1, n2)

        def reverse(n1, n2):
            left = n1
            right = n2
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        _len = len(nums)
        for i in range(_len - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                process(i - 1, _len - 1)
                return nums
        reverse(0, _len - 1)
        return nums


if __name__ == '__main__':
    # print(Solution().nextPermutation([4, 3, 2, 1]) == [1, 2, 3, 4])
    print(Solution().nextPermutation([1, 4, 3, 2]) == [2, 1, 3, 4])
    print(Solution().nextPermutation([10, 2, 3, 1, 6, 5, 4, 3, 2, 1]) == [10, 2, 3, 2, 1, 1, 3, 4, 5, 6])
    print(Solution().nextPermutation([10, 2, 3, 4, 6, 5, 4, 3, 2, 1]) == [10, 2, 3, 5, 1, 2, 3, 4, 4, 6])
    print(Solution().nextPermutation([10, 2, 3, 1, 6, 5, 4, 3, 2, 2]) == [10, 2, 3, 2, 1, 2, 3, 4, 5, 6])

    print(Solution().nextPermutation([3, 2, 1]) == [1, 2, 3])
    print(Solution().nextPermutation([1, 1, 5]) == [1, 5, 1])
    print(Solution().nextPermutation([1]) == [1])
    print(Solution().nextPermutation([1, 2, 3]) == [1, 3, 2])
