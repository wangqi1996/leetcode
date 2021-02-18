class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        count = [0 for _ in range(num + 1)]
        index, n, j = 1, 1, 0
        for i in range(1, num + 1):
            if i == n:
                j, n = 1, n * 2
                count[i] = 1
            else:
                count[i] = count[j] + 1
                j += 1
        return count


if __name__ == '__main__':
    print(Solution().countBits(2))
