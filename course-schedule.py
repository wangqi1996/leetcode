class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        count = [0 for _ in range(numCourses)]
        pre = {}
        for p1, p2 in prerequisites:
            pre.setdefault(p2, [])
            pre[p2].append(p1)
            count[p1] += 1

        stack = []
        result = 0
        for i in range(numCourses):
            if count[i] == 0:
                stack.append(i)
                result += 1

        while len(stack) > 0:
            course = stack.pop()
            for c in pre.get(course, []):
                count[c] -= 1
                if count[c] == 0:
                    stack.append(c)
                    result += 1

        return result == numCourses


if __name__ == '__main__':
    print(Solution().canFinish(2, [[1, 0], [0, 1]]))
