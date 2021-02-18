class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = None
        self.right = None

    def pre(self):
        s = ''
        s += str(self.val)
        if self.left:
            s += self.left.pre()
        if self.right:
            s += self.right.pre()
        return s


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q, s, index = [root], '', 0
        while index < len(q):
            root, index = q[index], index + 1
            if root:
                s += (str(root.val) + ',')
                q.extend([root.left, root.right])
            else:
                s += 'N,'
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        node = data.strip(',').split(',')
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
            if node[i] != 'N':
                root.left = TreeNode(int(node[i]), None, None)
                t.append(root.left)
            if i + 1 < _len and node[i + 1] != 'N':
                root.right = TreeNode(int(node[i + 1]), None, None)
                t.append(root.right)
            queue.extend(t)
            i += 2

        return queue[0]


if __name__ == '__main__':
    root = Codec().deserialize('1,2,3,N,N,4,5,N,N,N,N,')
    print(Codec().serialize(root))
