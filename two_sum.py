from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for index, num in enumerate(nums):
            if (target - num) in a:
                return [index, a[target - num]]
            a[num] = index
        # import numpy as np
        # index = np.argsort(nums)
        # nums = sorted(nums)
        # _len = len(nums)
        # for i in range(_len):
        #     for j in range(_len - 1, i, -1):
        #         if nums[j] + nums[i] < target:
        #             break
        #         if nums[j] + nums[i] == target:
        #             return [index[i], index[j]]
        #
        # return [-1, -1]


if __name__ == '__main__':
    print(Solution().twoSum([3, 3], 6))
    print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([2, 7, 11, 15], 9))
