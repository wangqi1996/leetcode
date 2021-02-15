# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        len1, len2 = 0, 0
        h1, h2 = headA, headB
        while h1:
            len1, h1 = len1 + 1, h1.next
        while h2:
            len2, h2 = len2 + 1, h2.next

        h1, h2 = headA, headB
        while len1 > len2:
            h1, len1 = h1.next, len1 - 1
        while len2 > len1:
            h2, len2 = h2.next, len2 - 1

        while h1 and h1 != h2:
            h1, h2 = h1.next, h2.next
        return h1

