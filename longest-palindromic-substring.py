class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        result = s[0]
        _len = len(s)
        for index, ss in enumerate(s[1:]):
            # case 1
            index += 1
            if s[index - 1] == ss:
                i, j = index - 2, index + 1
                while i >= 0 and j < _len and s[i] == s[j]:
                    i -= 1
                    j += 1
                if len(s[i + 1:j]) > len(result):
                    result = s[i + 1:j]
            # case 2
            i, j = index - 1, index + 1
            while i >= 0 and j < _len and s[i] == s[j]:
                i -= 1
                j += 1
            if len(s[i + 1:j]) > len(result):
                result = s[i + 1:j]

        return result


if __name__ == '__main__':
    # print(Solution().longestPalindrome("babad"))
    # print(Solution().longestPalindrome("abbd"))
    # print(Solution().longestPalindrome("a"))
    print(Solution().longestPalindrome("ac"))
    print(Solution().longestPalindrome("aA"))
    print(Solution().longestPalindrome("") + 'k')
    print(Solution().longestPalindrome(" ") + 'kl')
    print(Solution().longestPalindrome("  ") + 'k')
