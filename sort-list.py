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
    if len(l) == 0:
        return None
    head = ListNode(l[0], None)
    result = head
    for ll in l[1:]:
        head.next = ListNode(ll, None)
        head = head.next
    printL(result)
    return result


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        h, sublength, length = head, 1, 0
        while h:
            h, length = h.next, length + 1
        res = ListNode(0, head)
        while sublength < length:
            pre, h = res, res.next
            while h:
                # get h1
                h1 = h
                for i in range(sublength):
                    if h is not None:
                        h = h.next
                    else:
                        break
                if h is None:
                    break
                # get h2
                h2 = h
                l = 0
                for i in range(sublength):
                    if h is not None:
                        h, l = h.next, l + 1
                    else:
                        break
                # merge
                l1, l2 = sublength, l
                while l1 and l2:
                    if h1.val < h2.val:
                        pre.next, h1, l1 = h1, h1.next, l1 - 1
                    else:
                        pre.next, h2, l2 = h2, h2.next, l2 - 1
                    pre = pre.next
                pre.next = h1 if l1 else h2
                while l1:
                    l1, pre = l1 - 1, pre.next
                while l2:
                    l2, pre = l2 - 1, pre.next
                pre.next = h
            sublength *= 2
        return res.next

        # if not head:
        #     return None
        # node_list = []
        # while head:
        #     node_list.append(head)
        #     head = head.next
        # _len = len(node_list)
        # head = node_list
        #
        # def head_adjust(i, j):
        #     while i <= j:
        #         left_child = 2 * i + 1
        #         if left_child > j:
        #             return
        #         right_child = 2 * i + 2 if 2 * i + 2 <= j else left_child
        #         if head[i].val >= head[left_child].val and head[i].val >= head[right_child].val:
        #             return
        #         if head[left_child].val <= head[right_child].val:
        #             head[right_child].val, head[i].val = head[i].val, head[right_child].val
        #             i = right_child
        #         else:
        #             head[left_child].val, head[i].val = head[i].val, head[left_child].val
        #             i = left_child
        #
        # def heap_sort():
        #     # build the heap
        #     for i in range((_len - 2) // 2, -1, -1):
        #         head_adjust(i, _len - 1)
        #
        #     # sort
        #     for i in range(_len - 1, -1, -1):
        #         head[i].val, head[0].val = head[0].val, head[i].val
        #         head_adjust(0, i - 1)
        #
        # heap_sort()
        # for index in range(_len - 1):
        #     head[index].next = head[index + 1]
        # return head[0]


if __name__ == '__main__':
    root = create([-1, 5, 3, 4, 0])
    printL(Solution().sortList(root))
