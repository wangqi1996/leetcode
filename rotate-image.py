class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        _len = len(matrix)
        if _len < 2:
            return
        for i in range((_len + 1) // 2):
            for j in range((_len) // 2):
                a = _len - 1 - i
                b = _len - 1 - j
                matrix[i][j], matrix[j][a], matrix[a][b], matrix[b][i] = matrix[b][i], matrix[i][j], matrix[j][a], \
                                                                         matrix[a][b]
        return matrix


if __name__ == '__main__':
    print(Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
