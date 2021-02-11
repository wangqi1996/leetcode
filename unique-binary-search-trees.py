class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(n):
            C = C * 2 * (2 * i + 1) / (i + 2)
        return int(C)
        # if n == 0:
        #     return 1
        # notes = {}
        #
        # def _count(current, pre):
        #     if current == n:
        #         return 1
        #
        #     _max = min(n - current, pre * 2)
        #     _sum = 0
        #     for i in range(1, _max + 1):
        #         key = (pre * 2, i)
        #         if key not in notes:
        #             notes[key] = comb(pre * 2, i)
        #         _sum += (_count(current + i, i) * notes[key])
        #     return _sum
        #
        # return _count(1, 1)


if __name__ == '__main__':
    print(Solution().numTrees(3))
    print(Solution().numTrees(1))
    print(Solution().numTrees(2))
    print(Solution().numTrees(4))
    print(Solution().numTrees(0))
