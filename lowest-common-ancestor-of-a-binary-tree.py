# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def find(root):
            if root:
                node, f11, f21 = find(root.left)
                if node:
                    return node, True, True
                node, f12, f22 = find(root.right)
                if node:
                    return node, True, True
                contain_p = f11 + f12 >= 1 or node == p
                contain_q = f21 + f22 >= 1 or node == q
                if contain_p or contain_q:
                    return root, True, True
                return None, contain_p, contain_q

            return None, False, False

        node, _, _ = find(root)
        return root
