class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n <= 2:
            return n

        a = 1
        b = 2
        for i in range(n - 2):
            a, b = b, a + b

        return b


if __name__ == '__main__':
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(3))
