from math import comb


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 1 or n <= 1:
            return 1
        return comb(m + n - 2, min(m - 1, n - 1))


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))
