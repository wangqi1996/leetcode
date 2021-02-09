# Definition for singly-linked list.
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
    result.print(result)
    return result

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = l1
        _pre = 0
        while l1.next is not None and l2.next is not None:
            _sum = _pre + l1.val + l2.val
            l1.val = _sum % 10
            _pre = _sum // 10
            l1 = l1.next
            l2 = l2.next

        if l1.next is None:
            l1.next = l2.next
            l2.next = None

        _pre += l2.val
        while l1.next is not None:
            _sum = _pre + l1.val
            l1.val = _sum % 10
            _pre = _sum // 10
            l1 = l1.next

        _sum = _pre + l1.val
        l1.val = _sum % 10
        _pre = _sum // 10
        if _pre > 0:
            l1.next = ListNode(_pre, None)

        return result





if __name__ == '__main__':
    # ListNode().print(Solution().addTwoNumbers(create([2, 4, 9]), create([5, 6, 4, 9])))
    ListNode().print(Solution().addTwoNumbers(create([2, 4, 3]), create([5, 6, 4])))
    ListNode().print(Solution().addTwoNumbers(create([0]), create([5, 6, 4])))
    ListNode().print(Solution().addTwoNumbers(create([5]), create([5])))
    ListNode().print(Solution().addTwoNumbers(create([0]), create([0])))
    ListNode().print(Solution().addTwoNumbers(create([9, 9, 9, 9, 9, 9, 9]), create([9, 9, 9, 9])))
