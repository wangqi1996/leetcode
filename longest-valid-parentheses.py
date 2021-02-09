class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        正逆向遍历
        """
        max_length = 0
        left = 0
        right = 0
        for ss in s:
            if ss == '(':
                left += 1
            if ss == ')':
                right += 1
                if right == left:
                    max_length = max(max_length, right * 2)
                elif right > left:
                    left = 0
                    right = 0

        _len = len(s)
        left = 0
        right = 0
        for i in range(_len - 1, -1, -1):
            if s[i] == '(':
                left += 1
                if left == right:
                    max_length = max(max_length, right * 2)
                elif left > right:
                    left = 0
                    right = 0
            if s[i] == ')':
                right += 1

        return max_length

    def longestValidParentheses3(self, s):
        """
        :type s: str
        :rtype: int
        栈
        """
        max_length = 0
        stack = [-1]
        for index, ss in enumerate(s):
            if ss == '(':
                stack.append(index)
            if ss == ')':
                if len(stack) > 1:
                    stack.pop()
                    max_length = max(index - stack[-1], max_length)
                else:
                    stack.pop()
                    stack.append(index)
        return max_length

    def longestValidParentheses2(self, s):
        """
        :type s: str
        :rtype: int
        数组
        """
        _len = len(s)
        if _len <= 1:
            return 0
        dp = [0 for _ in range(_len)]
        for index, ss in enumerate(s[1:]):
            index += 1
            if ss == '(':
                continue

            pre = dp[index - 1]
            if (index - pre - 1) >= 0 and s[index - pre - 1] == '(':
                value = 2 + dp[index - 1]
                if index - pre - 2 > 0:
                    value += dp[index - pre - 2]
                dp[index] = value
        return max(dp)


if __name__ == '__main__':
    print(Solution().longestValidParentheses("(()") == 2)
    print(Solution().longestValidParentheses(")()())") == 4)
    print(Solution().longestValidParentheses("(())") == 4)
    print(Solution().longestValidParentheses("(()))())()") == 4)
    print(Solution().longestValidParentheses("(()))())(") == 4)
