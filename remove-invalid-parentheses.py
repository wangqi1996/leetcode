class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def is_valid(s):
            cnt = 0
            for ss in s:
                if ss == '(':
                    cnt += 1
                elif ss == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        queue = set([s])
        result = []
        while len(queue) > 0:
            new_queue = set()
            while len(queue) > 0:
                s = queue.pop()
                if is_valid(s):
                    result.append(s)
                if len(result) == 0:
                    for i in range(len(s)):
                        if s[i] == '(' or s[i] == ')':
                            new_queue.update([s[:i] + s[i + 1:]])
            queue = new_queue
        return result


if __name__ == '__main__':
    print(Solution().removeInvalidParentheses('(()()))()(()'))
