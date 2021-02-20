# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(vals):
    if len(vals) <= 0:
        return None
    head = TreeNode(vals[0], None, None)
    queue = [head]
    index, _len = 1, len(vals)
    while len(queue) >= 0:
        new_queue = []
        for q in queue:
            if index >= _len:
                return head
            val = vals[index]
            if val is not None:
                q.left = TreeNode(val, None, None)
            index += 1
            if index >= _len:
                return head
            val = vals[index]
            if val is not None:
                q.right = TreeNode(val, None, None)
            index += 1
            new_queue.extend([q.left, q.right])
        queue = new_queue

    return head


result = []


def preorder(root):
    if root:
        result.append(root.val)
        preorder(root.left)
        preorder(root.right)


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def rinorder(root, s):
            if root:
                s = rinorder(root.right, s)
                root.val += s
                s = rinorder(root.left, root.val)
                return s

            return s

        rinorder(root, 0)
        return root


if __name__ == '__main__':
    preorder(Solution().convertBST(build([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])))
    print(result)
