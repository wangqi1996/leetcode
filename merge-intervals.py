class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals

        intervals.sort()
        result = []
        start, end = intervals[0]
        for s, e in intervals:
            if s <= end:
                end = max(end, e)
            else:
                result.append([start, end])
                start, end = s, e
        result.append([start, end])
        return result


if __name__ == '__main__':
    print(Solution().merge([[1, 3], [2, 6], [15, 18], [8, 10]]))
