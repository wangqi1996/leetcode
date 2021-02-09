class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def match(a, b):
            if b == '.' or a == b:
                return True
            return False

        len_s = len(s)
        len_p = len(p)
        dp = [[False for _ in range(len_p + 1)] for _ in range(len_s + 1)]
        dp[0][0] = True

        for i in range(0, len_s + 1):
            for j in range(1, len_p + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if i > 0 and match(s[i - 1], p[j - 2]) and dp[i - 1][j]:
                        dp[i][j] = True
                else:
                    dp[i][j] = i > 0 and dp[i - 1][j - 1] and match(s[i - 1], p[j - 1])

        return dp[len_s][len_p]


if __name__ == '__main__':
    print(Solution().isMatch("aaa", "ab*a*c*a") is True)
    print(Solution().isMatch("aa", "a") is False)
    print(Solution().isMatch("aa", "a*") is True)
    print(Solution().isMatch("aa", "b*aa") is True)
    print(Solution().isMatch("aa", "a*aa") is True)
    print(Solution().isMatch("aa", "a*b*") is True)
    print(Solution().isMatch("aa", ".*") is True)
    print(Solution().isMatch("aab", "c*a*b") is True)
    print(Solution().isMatch("mississippi", "mis*is*p*.") is False)
    print(Solution().isMatch("mississippi", "mis*is*ip*.") is True)
