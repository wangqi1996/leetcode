class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        _len = len(s)
        dp = [[0 for _ in range(_len)] for _ in range(_len)]
        result = 0
        for i in range(_len):
            dp[i][i] = 1
            if i - 1 >= 0:
                dp[i][i - 1] = 1 if s[i] == s[i - 1] else 0
            if i - 2 >= 0:
                dp[i][i - 2] = 1 if s[i] == s[i - 2] else 0
            for j in range(i - 3, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = 1 if dp[i - 1][j + 1] == 1 else 0
        for i in range(_len):
            for j in range(i + 1):
                if dp[i][j] > 0:
                    result += 1
        return result


if __name__ == '__main__':
    print(Solution().countSubstrings("abaabaaba"))
