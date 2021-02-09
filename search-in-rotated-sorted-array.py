class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index, n in enumerate(nums):
            if n == target:
                return index
        return -1


if __name__ == '__main__':
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
    print(Solution().search([1], 0))
