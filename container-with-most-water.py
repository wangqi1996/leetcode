class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        _max = 0
        while i < j:
            _max = max(_max, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return _max


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(Solution().maxArea([1, 1]))
    print(Solution().maxArea([4, 3, 2, 1, 4]))
    print(Solution().maxArea([1, 2, 1]))
