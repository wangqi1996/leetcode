class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        _len1, _len2 = len(grid), len(grid[0])

        for i in range(0, _len1):
            for j in range(0, _len2):
                if i == 0 and j == 0:
                    continue
                elif j == 0:
                    grid[i][0] += grid[i - 1][0]
                elif i == 0:
                    grid[0][j] += grid[0][j - 1]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[_len1 - 1][_len2 - 1]


if __name__ == '__main__':
    print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
