class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return 0

        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                if j == 0:
                    matrix[i][j] = int(matrix[i][j])
                    continue

                matrix[i][j] = matrix[i][j - 1] + 1 if matrix[i][j] == "1" else 0

        def f(heights):
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

        result = 0
        for j in range(col):
            heights = [matrix[i][j] for i in range(row)]
            result = max(result, f(heights))

        return result


if __name__ == '__main__':
    print(Solution().maximalRectangle([['1']]))
