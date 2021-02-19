# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def max_depth(root):
            if root:
                l1, left = max_depth(root.left)
                r1, right = max_depth(root.right)
                return max(left + right, l1, r1), max(left, right)
            return 0, 0

        l1, l2 = max_depth(root)
        return max(l1, l2)
