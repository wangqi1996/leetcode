class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) <= 0 or len(matrix[0]) <= 0:
            return False
        len_row, len_col = len(matrix), len(matrix[0])

        left, up = len_col - 1, 0
        while left >= 0 and up <= len_row - 1:
            if matrix[up][left] == target:
                return True
            if matrix[up][left] < target:
                up += 1
            else:
                left -= 1
        return False
        # def binary_search(row):
        #     low, high = 0, len_col - 1
        #     if matrix[row][0] > target or matrix[row][len_col - 1] < target:
        #         return False
        #     while low <= high:
        #         mid = (low + high) // 2
        #         if matrix[row][mid] == target:
        #             return True
        #         if matrix[row][mid] < target:
        #             low = mid + 1
        #         else:
        #             high = mid - 1
        #
        # for i in range(len_row):
        #     if binary_search(i):
        #         return True
        # return False


if __name__ == '__main__':
    print(Solution().searchMatrix(
        [[1, 4, 7, 11, 15]], 11))
