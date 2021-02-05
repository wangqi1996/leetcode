class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        max_len = 1
        start = 0
        for end, ss in enumerate(s[1:]):
            if ss in s[start: end + 1]:
                index = s[start: end + 1].index(ss)
                start += (index + 1)
            max_len = max(max_len, end - start + 2)

        return max_len


if __name__ == '__main__':
    # print(Solution().lengthOfLongestSubstring("abcabcbb"))
    # print(Solution().lengthOfLongestSubstring("bbbbb"))
    # print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring(" "))
    print(Solution().lengthOfLongestSubstring(""))