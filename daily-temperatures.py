class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        point = [40000 for _ in range(101)]
        _max, _len = T[-1], len(T)
        point[T[-1]] = _len - 1
        result = [0 for _ in range(_len)]
        for i in range(_len - 2, -1, -1):
            point[T[i]] = i
            if T[i] >= _max:
                _max = T[i]
            else:
                if (_len - i) > 70:
                    next = min(point[T[i] + 1:_max + 1])
                    result[i] = next - i
                else:
                    for j in range(i + 1, _len):
                        if T[j] > T[i]:
                            result[i] = j - i
                            break
        return result


if __name__ == '__main__':
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
