class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
                   '8': 'tuv', '9': 'wxyz'}

        if len(digits) < 1:
            return []

        result = ['']
        for d in digits:
            result = [pre + mm for pre in result for mm in mapping[d]]
        # def f(dig, prefix):
        #     m = mapping[dig[0]]
        #     if len(dig) == 1:
        #         for mm in m:
        #             result.append(prefix + mm)
        #     else:
        #         for mm in m:
        #             f(dig[1:], prefix + mm)

        # f(digits, '')
        return result


if __name__ == '__main__':
    print(Solution().letterCombinations('23'))
    print(Solution().letterCombinations(''))
    print(Solution().letterCombinations('2'))
