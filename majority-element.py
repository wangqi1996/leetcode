class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        candidate = 0
        for n in nums:
            if c == 0:
                candidate = n
                c = 1
            else:
                c = c + 1 if n == candidate else c - 1
        return candidate


print(Solution().majorityElement([1, 2, 3, 4, 4, 4, 4, 4, 4, 6, 6, 6]))
