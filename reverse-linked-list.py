# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        def _reverse(head):
            if not head.next:
                return head
            h = _reverse(head.next)
            head.next.next = head
            head.next = None
            return h

        h = _reverse(head)
        return h

        # if not head:
        #     return None
        # pre, cur, next = None, head, head.next
        # while cur:
        #     next = cur.next
        #     cur.next = pre
        #     pre, cur = cur, next
        # return pre
