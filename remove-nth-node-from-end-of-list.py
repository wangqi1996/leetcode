class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self, r):
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
    # result.print(result)
    return result


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = []
        result = head
        while head is not None:
            l.append(head)
            head = head.next
        _len = len(l)
        if n == _len:
            return result.next
        if n == 1:
            l[-2].next = None
            return result
        pre = l[_len - n - 1]
        next = l[_len - n + 1]
        pre.next = next
        return result


if __name__ == '__main__':
    ListNode().print(Solution().removeNthFromEnd(create([1, 2, 3, 4, 5]), 2))
    ListNode().print(Solution().removeNthFromEnd(create([1, 2, 3, 4, 5]), 1))
    ListNode().print(Solution().removeNthFromEnd(create([1, 2, 3, 4, 5]), 5))
    ListNode().print(Solution().removeNthFromEnd(create([1]), 1))
    ListNode().print(Solution().removeNthFromEnd(create([1, 2]), 1))
