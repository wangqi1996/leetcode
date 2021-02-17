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


def create(l):
    if len(l) <= 0:
        return None
    head = ListNode(l[0], None)
    result = head
    for ll in l[1:]:
        head.next = ListNode(ll, None)
        head = head.next
    return result


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        fast, slow = head.next, head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next

        pre, slow = slow, slow.next
        pre.next = None

        if slow:
            while slow:
                next, slow.next = slow.next, pre
                pre, slow = slow, next

        left, right = head, pre
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome(create([])) is True)
    print(Solution().isPalindrome(create([1, 3, 1])))
    print(Solution().isPalindrome(create([1, 1])))
    print(Solution().isPalindrome(create([1, 2, 2, 1])))
    print(Solution().isPalindrome(create([1, 2])))
    print(Solution().isPalindrome(create([1])))

    print(Solution().isPalindrome(create([1, 23, 3, 2, 1])))
