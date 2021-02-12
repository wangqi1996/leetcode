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
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        inf = float('-inf')

        def _maxpathsum(root):
            if root is None:
                return inf, inf
            if root.left is None and root.right is None:
                return root.val, root.val
            max_left, _max1 = _maxpathsum(root.left)
            max_right, _max2 = _maxpathsum(root.right)
            current_max = max(max_left, max_right, 0) + root.val
            _max = max(max_left + max_right + root.val, current_max, _max1, _max2)
            return current_max, _max

        _, _max = _maxpathsum(root)
        return _max


if __name__ == '__main__':
    root = build([-1])
    print(Solution().maxPathSum(root))
    root = build([-2, -1])
    print(Solution().maxPathSum(root))
    root = build([-10, 9, 20, None, None, 15, 7])
    print(Solution().maxPathSum(root))
    root = build([2, 1, 3])
    print(Solution().maxPathSum(root))
