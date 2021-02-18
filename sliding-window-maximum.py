class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        """
        分块+预处理
        """
        if k == 1:
            return nums
        _len = len(nums)
        n_k = _len // k + 1 if _len % k != 0 else _len // k
        pre = [0 for _ in range(_len)]
        suf = [0 for _ in range(_len)]
        for block in range(n_k):
            start = block * k
            end = min((block + 1) * k, _len)
            pre[start] = nums[start]
            for j in range(start + 1, end):
                pre[j] = max(nums[j], pre[j - 1])
            suf[end - 1] = nums[end - 1]
            for j in range(end - 2, start - 1, -1):
                suf[j] = max(suf[j + 1], nums[j])
        result = []
        for i in range(k - 1, _len):
            result.append(max(pre[i], suf[i - k + 1]))
        return result

        """
        单调队列
        """
        # if k == 1:
        #     return nums
        # import collections
        # q = collections.deque()
        # _len = len(nums)
        # for i in range(0, k):
        #     while len(q) > 0 and nums[i] >= nums[q[-1]]:
        #         q.pop()
        #     q.append(i)
        # result = [nums[q[0]]]
        # for i in range(k, _len):
        #     if q[0] <= (i - k):
        #         q.popleft()
        #     while len(q) > 0 and nums[i] >= nums[q[-1]]:
        #         q.pop()
        #     q.append(i)
        #     result.append(nums[q[0]])
        # return result
        """
        用堆解决: 优先队列
        """
        # if k == 1:
        #     return nums
        # import heapq
        # heap = [(-nums[i], i) for i in range(k)]
        # heapq.heapify(heap)
        # _len = len(nums)
        # result = [-heap[0][0]]
        # for i in range(k, _len):
        #     while heap[0][1] <= i - k:
        #         heapq.heappop(heap)
        #     heapq.heappush(heap, (-nums[i], i))
        #     v = -heap[0][0]
        #     result.append(v)
        # return result


if __name__ == '__main__':
    print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
