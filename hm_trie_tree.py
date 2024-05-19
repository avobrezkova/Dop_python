class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def delete(self, word):
        def _delete_helper(node, word, depth):
            if depth == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                if not node.children:
                    return True
                return False
            char = word[depth]
            if char in node.children:
                if _delete_helper(node.children[char], word, depth + 1):
                    del node.children[char]
                    return not node.children
            return False

        if not self.search(word):
            return False
        _delete_helper(self.root, word, 0)
        return True

# Пример использования
trie = Trie()
trie.insert("film")
trie.insert("series")
print(trie.search("film"))  # Output: True
print(trie.search("series"))  # Output: True

trie.delete("series")
print(trie.search("series"))  # Output: False