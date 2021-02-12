# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next):
        self.val = x
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
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        key = "fefewfge"
        while head:
            if head.val == key:
                return True
            head.val = key

        return False


if __name__ == '__main__':
    print(Solution().hasCycle(create([3, 2, 0, 4])))
