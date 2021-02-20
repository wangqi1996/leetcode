class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        _len = len(nums)
        dict = {0: 1}
        r, pre = 0, 0
        for i in range(_len):
            pre += nums[i]
            diff = pre - k
            r += dict.get(diff, 0)
            dict.setdefault(pre, 0)
            dict[pre] += 1

        return r


if __name__ == '__main__':
    print(Solution().subarraySum([1, 1, 1], 2))
