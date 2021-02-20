class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        start = {}
        end = {}
        for index, n in enumerate(nums):
            dict.setdefault(n, 0)
            dict[n] += 1
            if n not in start:
                start[n] = index
            end[n] = index
        _max, _max_index = 0, []
        for n, count in dict.items():
            if count > _max:
                _max = count
                _max_index = [n]
            elif count == _max:
                _max_index.append(n)
        r = end[_max_index[0]] - start[_max_index[0]] + 1
        for rr in _max_index[1:]:
            r = min(r, end[rr] - start[rr] + 1)
        return r


if __name__ == '__main__':
    print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))
