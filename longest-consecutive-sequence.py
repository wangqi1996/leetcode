class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        _len = len(numset)
        _max = 0
        for n in numset:
            if n - 1 not in numset:
                for i in range(1, _len + 1):
                    if i + n not in numset:
                        break
                _max = max(_max, i)
        return _max


if __name__ == '__main__':
    print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
