class TrieNode:
    def __init__(self):
        """ initialize a node within a Trie """
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        """ Initialize the root of the Trie """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """ Insert a word into the Trie """
        current = self.root
        for letter in range(len(word)):
            # if the current letter is not a child of the root
            if word[letter] not in current.children:
                current.children[word[letter]] = TrieNode()
            # set new current to previous child 
            current = current.children[word[letter]]
            # if this is the last letter in the word, mark it as so
            if letter == len(word) - 1:
                current.endOfWord = True

    def search(self, word: str) -> bool:
        """ Search for a word inside the Trie """
        current = self.root
        for letter in range(len(word)):
            # if the letter is not in, or its the last letter but not the end of the word return F
            if word[letter] not in current.children:
                return False
            current = current.children[word[letter]]
            if ((letter == len(word) - 1) and not current.endOfWord):
                return False
        return True
    
    def startsWith(self, prefix: str) -> bool:
        """ See if theres a word that starts with prefix """
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
    



class TrieNode:
    def __init__(self):
        """ initialize a node within a Trie """
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        """ Initialize the root of the Trie """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """ Insert a word into the Trie """
        current = self.root
        for letter in word:
            # if the current letter is not a child of the root
            if letter not in current.children:
                current.children[letter] = TrieNode()
            # set new current to previous child 
            current = current.children[letter]
        current.endOfWord = True

    def search(self, word: str) -> bool:
        """ Search for a word inside the Trie """
        current = self.root
        for letter in word:
            # if the letter is not in, or its the last letter but not the end of the word return F
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.endOfWord
    
    def startsWith(self, prefix: str) -> bool:
        """ See if theres a word that starts with prefix """
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)