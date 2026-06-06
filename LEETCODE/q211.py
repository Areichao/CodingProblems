class Trie:
    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if ch not in node.child:
                node.child[ch] = Trie()
            node = node.child[ch]
        node.end = True
            

    def search(self, word: str) -> bool:
        def _search2(word: str, node: Trie) -> bool:
            for i, ch in enumerate(word):
                if ch == ".":
                    for child_node in node.child.values():
                        if _search2(word[i + 1:], child_node):
                            return True
                    return False

                if ch not in node.child:
                    return False

                node = node.child[ch]

            return node.end

        return _search2(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)