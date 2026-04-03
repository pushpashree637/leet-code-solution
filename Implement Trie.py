class Trie:
    def __init__(self):
        self.words = []
    def insert(self, word):
        self.words.append(word)
        return None
    def search(self, word):
        return word in self.words

    def startsWith(self, prefix):
        for w in self.words:
            if w.startswith(prefix):
                return True
        return False
trie = Trie()
output = []
output.append(None) 
output.append(trie.insert("apple"))
output.append(trie.search("apple"))
output.append(trie.search("app"))
output.append(trie.startsWith("app"))
output.append(trie.insert("app"))
output.append(trie.search("app"))
print(output)
