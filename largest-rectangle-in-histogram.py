class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1, 0]
        _len = len(heights)
        _max = 0
        for i in range(1, _len):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while heights[stack[-1]] > heights[i]:
                    v = stack.pop()
                    _max = max(_max, heights[v] * (i - stack[-1] - 1))
                stack.append(i)
        return _max

        # _len = len(heights)
        # _max = 0
        # for index in range(_len):
        #     j = index
        #     flag = False
        #     while j > 0 and heights[j - 1] >= heights[index]:
        #         if heights[j - 1] == heights[index]:
        #             flag = True
        #             break
        #         j -= 1
        #
        #     if flag:
        #         continue
        #     width = index - j + 1
        #     j = index
        #     while j < _len - 1 and heights[j + 1] >= heights[index]:
        #         j += 1
        #     width += (j - index)
        #     _max = max(_max, width * heights[index])
        # return _max


if __name__ == '__main__':
    print(Solution().largestRectangleArea([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
