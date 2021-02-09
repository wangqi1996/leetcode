class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = ['(']
        num = [1]
        for _ in range(1, 2 * n):
            new_result = []
            new_num = []
            for r, current_n in zip(result, num):
                if current_n < n:
                    new_result.append(r + '(')
                    new_num.append(current_n + 1)
                current_n2 = len(r) - current_n
                if current_n2 < current_n:
                    new_result.append(r + ')')
                    new_num.append(current_n)
            result = new_result
            num = new_num

        return result


if __name__ == '__main__':
    print(Solution().generateParenthesis(1))
    print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(2))
