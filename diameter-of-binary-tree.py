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
            if root.left:
                l1, left = max_depth(root.left)
                left += 1
            else:
                l1, left = 0, 0
            if root.right:
                r1, right = max_depth(root.right)
                right += 1
            else:
                r1, right = 0, 0
            return max(left + right, l1, r1), max(left, right)

        if not root:
            return 0
        l1, l2 = max_depth(root)
        return max(l1, l2)
