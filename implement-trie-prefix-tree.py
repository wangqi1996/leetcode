class TrieNode(object):
    def __init__(self, val):
        self.child = {}
        self.val = val

    def build_child(self, val):
        if val in self.child:
            return self.child[val]
        child = TrieNode(val)
        self.child[val] = child
        return self.child[val]

    def get_child(self, val):
        return self.child.get(val, None)


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')
        self.end_key = "end"

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        root = self.root
        for w in word:
            root = root.build_child(w)
        root.build_child("end")

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for w in word:
            root = root.get_child(w)
            if not root:
                return False
        root = root.get_child("end")
        return root is not None

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        for w in prefix:
            root = root.get_child(w)
            if not root:
                return False
        return True


# Your Trie object will be instantiated and called as such:
if __name__ == '__main__':
    word = "apple"
    prefix = "app"
    obj = Trie()
    obj.insert(word)
    param_2 = obj.search(word)
    param_3 = obj.startsWith(prefix)
    print(param_2, param_3)
    print(obj.search("adjiowe"))
    print(obj.startsWith("ew"))
