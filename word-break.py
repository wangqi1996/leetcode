class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        _len = len(s)
        dp = [False for _ in range(_len)]
        for i in range(_len):
            if i == 0 and s[i] in wordDict:
                dp[i] = True
            for j in range(i, -1, -1):
                if j == 0 and s[:i + 1] in wordDict:
                    dp[i] = True
                elif dp[j - 1] and s[j:i + 1] in wordDict:
                    dp[i] = True
        return dp[-1]
        # _len = len(s)
        # error = []
        #
        # def _break(index):
        #     if index >= _len:
        #         return True
        #     if s[index:] in error:
        #         return False
        #     for i in range(index, _len):
        #         if s[index:i + 1] in wordDict and _break(i + 1):
        #             return True
        #         else:
        #             error.append(s[index:])
        #     return False
        #
        # return _break(0)


if __name__ == '__main__':
    print(Solution().wordBreak("ab", ["a", "b"]))
