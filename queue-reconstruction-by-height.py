class Solution(object):
    def reconstructQueue(self, people: list):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (x[0], -x[1]))
        _len = len(people)
        result = [None for _ in range(_len)]
        for h, k in people:
            r, i = 0, 0
            while i < _len and r <= k:
                if result[i] is None:
                    r += 1
                i += 1
            result[i - 1] = [h, k]
        return result


if __name__ == '__main__':
    print(Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
