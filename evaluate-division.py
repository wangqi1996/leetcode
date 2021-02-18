class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        valid_x = set()
        for eq in equations:
            valid_x.update([eq[0], eq[1]])
        relation = [[None for _ in range(len(valid_x))] for _ in range(len(valid_x))]
        m = {v: i for i, v in enumerate(valid_x)}
        _len = len(valid_x)
        for eq, v in zip(equations, values):
            relation[m[eq[0]]][m[eq[1]]] = v
            relation[m[eq[1]]][m[eq[0]]] = 1 / v
        for k in range(_len):
            for i in range(_len):
                for j in range(_len):
                    if i == j:
                        relation[i][j] = 1
                    if relation[i][j] is None and relation[i][k] is not None and relation[k][j] is not None:
                        relation[i][j] = relation[i][k] * relation[k][j]
        result = []
        for q1, q2 in queries:
            if q1 in valid_x and q2 in valid_x and relation[m[q1]][m[q2]] is not None:
                result.append(relation[m[q1]][m[q2]])
            else:
                result.append(-1.0)
        return result


if __name__ == '__main__':
    print(Solution().calcEquation([["a", "b"], ["b", "c"]], [2, 3],
                                  [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
