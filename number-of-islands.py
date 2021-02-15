class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        len_row = len(grid)
        len_col = len(grid[0])
        visited = [[False for _ in range(len_col)] for _ in range(len_row)]
        result = 0
        for r in range(len_row):
            for c in range(len_col):
                if grid[r][c] == '1' and not visited[r][c]:
                    result += 1
                    queue = [(r, c)]
                    visited[r][c] = True
                    while len(queue) > 0:
                        i, j = queue.pop()
                        for i_d, j_d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            _i, _j = i + i_d, j + j_d
                            if 0 <= _i < len_row and 0 <= _j < len_col and grid[_i][_j] == '1' and not visited[_i][_j]:
                                visited[_i][_j] = True
                                queue.append((_i, _j))
        return result


if __name__ == '__main__':
    print(Solution().numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
