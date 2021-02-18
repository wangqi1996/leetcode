class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, _len = [], len(s)
        res, times = '', 0
        for i in range(_len):
            if s[i].isdigit():
                times = times * 10 + int(s[i])
            elif s[i] == '[':
                stack.append((times, res))
                times, res = 0, ''
            elif s[i] == ']':
                times2, res2 = stack.pop()
                res = res2 + times2 * res
            else:
                res += s[i]
        return res


if __name__ == '__main__':
    print(Solution().decodeString('2[abc]3[cd]ef'))
