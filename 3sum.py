class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        _len = len(nums)

        for i in range(_len):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j, k = i + 1, _len - 1
            diff = -nums[i]
            while j < k:
                if nums[j] + nums[k] == diff:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < _len and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[j] + nums[k] < diff:
                    j += 1
                else:
                    k -= 1

        return result


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum([]))
    print(Solution().threeSum([0]))
    print(Solution().threeSum([0, 0]))
    print(Solution().threeSum([0, 0, 0]))
