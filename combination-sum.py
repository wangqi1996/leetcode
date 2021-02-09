class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        _len = len(candidates)
        candidates.sort()

        def combina(index, current, l):
            if current > target or index == _len:
                return

            if current == target:
                result.append(l)
                return result

            combina(index, current + candidates[index], l + [candidates[index]])
            combina(index + 1, current, l)

        combina(0, 0, [])
        return result


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
    print(Solution().combinationSum([2, 3, 5], 8))
    print(Solution().combinationSum([2], 2))
    print(Solution().combinationSum([2], 4))
    print(Solution().combinationSum([2], 1))
