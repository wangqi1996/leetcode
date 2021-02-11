class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 0:
            return [[]]

        result = [[], [nums[0]]]
        for n in nums[1:]:
            result = [r + a for a in [[], [n]] for r in result]
        return result


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
