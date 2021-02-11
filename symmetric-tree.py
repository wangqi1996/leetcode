# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(l):
    

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        layer = [root]
        while len(layer) > 0:
            temp = []
            for n in layer:
                if n:
                    temp.extend([n.left, n.right])
            _len = len(temp)
            for i in range(_len // 2):
                if temp[i] != temp[_len - 1 - i]:
                    return False

            layer = temp

        return True


if __name__ == '__main__':
    print(Solution().isSymmetric())
