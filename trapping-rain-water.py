class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0

        _len = len(height)
        left_max = [0 for _ in range(_len)]
        _max = 0
        for index, h in enumerate(height[:-1]):
            if h > _max:
                _max = h
            left_max[index + 1] = _max
        _sum = 0
        _max = 0
        for index in range(_len - 1, 0, -1):
            if height[index] > _max:
                _max = height[index]
            _sum += max(min(left_max[index], _max) - height[index], 0)
        return _sum


if __name__ == '__main__':
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution().trap([4, 2, 0, 3, 2, 5]))
