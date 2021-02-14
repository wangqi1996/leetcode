# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printL(r):
    s = ''
    while r is not None:
        s += (str(r.val) + ' -> ')
        r = r.next
        print(s)
    print(s)


def create(l):
    if len(l) == 0:
        return None
    head = ListNode(l[0], None)
    result = head
    pre = None
    for ll in l[1:]:
        head.next = ListNode(ll, None)
        pre = head
        head = head.next
    pre.next = result.next
    # printL(result)
    return result


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None

        slow = head
        fast = head.next
        while slow and fast != slow:
            slow = slow.next
            for i in range(2):
                if fast.next is None:
                    return None
                else:
                    fast = fast.next

        if slow:
            slow = slow.next
            ptr = head
            while ptr != slow:
                slow = slow.next
                ptr = ptr.next
            return ptr
        return None


if __name__ == '__main__':
    root = create([3, 2, 0, -4])
    print(Solution().detectCycle(root).val)
