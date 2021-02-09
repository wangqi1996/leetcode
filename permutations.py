from typing import List


class Solution(object):
    def permute(self, nums: List):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        _len = len(nums)

        result = []

        def backtrack(used, current_len, path):
            if current_len == _len:
                result.append(path)
                return
            for i in range(_len):
                if not used[i]:
                    used[i] = True
                    backtrack(used, current_len + 1, path + [nums[i]])
                    used[i] = False

        used = [False for _ in range(_len)]
        backtrack(used, 0, [])
        return result


if __name__ == '__main__':
    print(Solution().permute([11, 12, 13]))
    print(Solution().permute([11]))
    print(Solution().permute([]))
