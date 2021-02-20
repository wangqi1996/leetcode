class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        lsum, rsum, _len = 0, 0, len(A)
        left, right, ans = 0, 0, 0
        while right < _len:
            rsum += 1 - A[right]
            while lsum < rsum - K:
                lsum += 1 - A[left]
                left += 1
            ans = max(right - left + 1, ans)
            right += 1
        return ans


if __name__ == '__main__':
    print(Solution().longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
    print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
    print(Solution().longestOnes([0, 0, 0, 1], 4))
