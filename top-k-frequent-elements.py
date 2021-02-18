class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for n in nums:
            count.setdefault(n, 0)
            count[n] += 1
        item = [(-v, k) for k, v in count.items()]
        import heapq
        heapq.heapify(item)
        r = heapq.nsmallest(k, item)
        return [rr[1] for rr in r]


if __name__ == '__main__':
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
