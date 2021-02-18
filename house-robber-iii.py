# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


def deserialize(node):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    if len(node) <= 0:
        return None
    head = TreeNode(int(node[0]), None, None)
    queue = [head]
    index = 0
    i, _len = 1, len(node)
    while i < _len:
        root = queue[index]
        index += 1
        t = []
        if node[i]:
            root.left = TreeNode(int(node[i]), None, None)
            t.append(root.left)
        if i + 1 < _len and node[i + 1]:
            root.right = TreeNode(int(node[i + 1]), None, None)
            t.append(root.right)
        queue.extend(t)
        i += 2

    return queue[0]


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def _rob(root):
            if root:
                c_left, n_left = _rob(root.left) if root.left else (0, 0)
                c_right, n_right = _rob(root.right) if root.right else (0, 0)
                non_contain = c_left + c_right
                contain = max(n_left + n_right + root.val, non_contain)
                return contain, non_contain
            return 0, 0

        return max(_rob(root))


if __name__ == '__main__':
    print(Solution().rob(deserialize([4, 1, None, 2, None, 3])))
