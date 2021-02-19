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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        # 递归遍历所有的路径
        def _path(root, current_sum):
            s = 0
            if root:
                new = []
                for c in current_sum:
                    new.append(c + root.val)
                new.append(root.val)
                for c in new:
                    if c == sum:
                        s += 1
                s1 = _path(root.left, new)
                s2 = _path(root.right, new)
                return s + s1 + s2
            else:
                return 0
        if root is None:
            return 0
        return _path(root.left, [root.val]) + _path(root.right, [root.val]) + int(root.val == sum)


if __name__ == '__main__':
    print(Solution().pathSum(build([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8))
