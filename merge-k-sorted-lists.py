# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print2(r: ListNode):
    s = ''
    while r is not None:
        s += (str(r.val) + ' -> ')
        r = r.next
    print(s)


def create(l):
    head = ListNode(l[0], None)
    result = head
    for ll in l[1:]:
        head.next = ListNode(ll, None)
        head = head.next
    return result


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        if not lists or len(lists) < 0:
            return None

        result = ListNode(-1, None)
        head = result
        _headq = []
        for index, l in enumerate(lists):
            if l:
                heapq.heappush(_headq, (l.val, index))
        while len(_headq):
            min_value, min_index = heapq.heappop(_headq)
            result.next = lists[min_index]
            if lists[min_index].next:
                lists[min_index] = lists[min_index].next
                heapq.heappush(_headq, (lists[min_index].val, min_index))

            result = result.next
        return head.next


if __name__ == '__main__':
    print2(Solution().mergeKLists([create([1, 4, 5]), create([1, 3, 4]), create([2, 6])]))
    print2(Solution().mergeKLists(None))
    print2(Solution().mergeKLists([]))
    print2(Solution().mergeKLists([None]))
    print2(Solution().mergeKLists([create([1, 4, 5]), None, create([1, 3, 4]), create([2, 6])]))
