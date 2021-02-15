class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        _heap = []
        for n in nums:
            heapq.heappush(_heap, n)
        return heapq.nlargest(k, _heap)

