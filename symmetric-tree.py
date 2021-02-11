# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # if not root:
        #     return True
        # layer = [root]
        # while len(layer) > 0:
        #     _len = len(layer)
        #     for i in range(_len // 2):
        #         if not layer[i] and not layer[_len - i - 1]:
        #             continue
        #         if not layer[i] or not layer[_len - i - 1] or layer[i].val != layer[_len - i - 1].val:
        #             return False
        #     new_list = []
        #     for node in layer:
        #         if node:
        #             new_list.extend([node.left, node.right])
        #     layer = new_list
        #
        # return True

        def check(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and check(node1.left, node2.right) and check(node2.left, node1.right)

        return check(root, root)


if __name__ == '__main__':
    print(Solution().isSymmetric())
