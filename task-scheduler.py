class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dict = {}
        for t in tasks:
            dict.setdefault(t, 0)
            dict[t] += 1
        t = list(dict.values())
        _max = max(t)
        c = t.count(_max)
        return max(len(tasks), (n + 1) * (_max - 1) + c)


if __name__ == '__main__':
    print(Solution().leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
