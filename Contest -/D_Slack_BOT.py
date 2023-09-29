n = int(input())
class TrieNode:
    def __init__(self):
        self.is_visited = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            else:
                curr.children[char].is_visited = True
            curr = curr.children[char]
    
    def search_count(self, word):
        curr = self.root
        count = 0
        for char in word:
            if char not in curr.children or not curr.children[char].is_visited:
                return count
            else:
                count += 1
            curr = curr.children[char]
        return count
    
trie = Trie()
arr = []
for i in range(n):
    word_input = input()
    arr.append(word_input)
    trie.insert(word_input)

for i in range(n):
    print(trie.search_count(arr[i]))