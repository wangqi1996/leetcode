class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) < 1:
            return len(word2)

        if len(word2) < 1:
            return len(word1)

        len_1 = len(word1)
        len_2 = len(word2)
        dp = [[0 for _ in range(len_2 + 1)] for _ in range(len_1 + 1)]
        for i in range(0, len_1 + 1):
            for j in range(0, len_2 + 1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i - 1][j - 1] + (word2[j - 1] != word1[i - 1])
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        return dp[len_1][len_2]


if __name__ == '__main__':
    print(Solution().minDistance("horse", "ros"))
    print(Solution().minDistance("intention", "execution"))
    print(Solution().minDistance("intention", "execution"))
    print(Solution().minDistance("intention", "execution"))
