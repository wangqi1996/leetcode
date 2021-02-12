from functools import reduce


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda a, b: a ^ b, nums)


if __name__ == '__main__':
    print(Solution().singleNumber([2, 2, 1]))
