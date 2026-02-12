class Node:
    __slot__ = 'son','end','count'

    def __init__(self):
        self.son = {}
        self.count = 0
        self.end = 0
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node()
            cur = cur.son[c]
            cur.count+=1
        cur.end+=1

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c not in cur.son:
                return 0
            cur = cur.son[c]
        return cur.end

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.son:
                return 0
            cur = cur.son[c]
        return cur.count

    def erase(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.son[c]
            cur.count-=1
        cur.end-=1

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)