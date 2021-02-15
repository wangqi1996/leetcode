class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        len_row, len_col = len(matrix), len(matrix[0])
        result = 0
        dp = [[1 for _ in range(len_col)] for _ in range(len_row)]
        for i in range(0, len_row):
            for j in range(0, len_col):
                matrix[i][j] = int(matrix[i][j])
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1 if matrix[i][j] == 1 else 0
                result = max(dp[i][j], result)
        return result * result

        # len_row, len_col = len(matrix), len(matrix[0])
        # result = 0
        # for i in range(0, len_row):
        #     matrix[i][0] = int(matrix[i][0])
        #     for j in range(1, len_col):
        #         matrix[i][j] = int(matrix[i][j])
        #         matrix[i][j] = matrix[i][j - 1] * matrix[i][j] + matrix[i][j]
        # matrix.append([0 for _ in range(len_col)])
        # for j in range(0, len_col):
        #     stack = [-1, 0]
        #     for i in range(1, len_row + 1):
        #         if matrix[i][j] >= matrix[stack[-1]][j]:
        #             stack.append(i)
        #         else:
        #             while matrix[i][j] < matrix[stack[-1]][j]:
        #                 index = stack.pop()
        #                 width = min(i - stack[-1] - 1, matrix[index][j])
        #                 result = max(result, width * width)
        #             stack.append(i)
        #
        # return result


if __name__ == '__main__':
    print(Solution().maximalSquare(
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    ))
    print(Solution().maximalSquare(
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
    print(Solution().maximalSquare(
        [["0", "0", "0", "1"], ["1", "1", "0", "1"], ["1", "1", "1", "1"], ["0", "1", "1", "1"], ["0", "1", "1", "1"]]))
