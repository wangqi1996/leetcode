# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def invert(root):
            if root:
                invert(root.left)
                invert(root.right)
                root.left, root.right = root.right, root.left

        invert(root)
