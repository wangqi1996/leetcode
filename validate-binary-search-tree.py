# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def _valid(root):
            min_left = root.val
            if root.left:
                min_left, max_left, valid = _valid(root.left)
                if not valid or max_left >= root.val:
                    return 0, 0, False
            max_right = root.val
            if root.right:
                min_right, max_right, valid = _valid(root.right)
                if not valid or root.val >= min_right:
                    return 0, 0, False
            return min(min_left, root.val), max(max_right, root.val), True

        if root:
            _, _, valid = _valid(root)
            return valid
        return True


