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
    if len(l) == 0:
        return None
    head = ListNode(l[0], None)
    result = head
    for ll in l[1:]:
        head.next = ListNode(ll, None)
        head = head.next
    # result.print(result)
    return result


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0, None)
        result = head
        while l1 and l2:
            if l1.val <= l2.val:
                result.next = l1
                l1 = l1.next
            else:
                result.next = l2
                l2 = l2.next
            result = result.next
        if l1:
            result.next = l1

        if l2:
            result.next = l2

        return head.next


if __name__ == '__main__':
    ListNode().print(Solution().mergeTwoLists(create([1, 2, 4]), create([1, 3, 4])))
    ListNode().print(Solution().mergeTwoLists(create([]), create([1, 3, 4])))
    ListNode().print(Solution().mergeTwoLists(create([]), create([])))
    ListNode().print(Solution().mergeTwoLists(create([1, 2, 4]), create([])))

