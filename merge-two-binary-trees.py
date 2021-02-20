# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        def _merge(root1, root2):
            if root1 and root2:
                root1.val = root1.val + root2.val
                root1.left = _merge(root1.left, root2.left)
                root1.right = _merge(root1.left, root2.left)
                return root1
            return root1 if root1 else root2
        return _merge(root1, root2)
