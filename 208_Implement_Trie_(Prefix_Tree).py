'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
'''


class Trie:
    class TrieNode:
        def __init__(self):
            self.childs = [None] * 26
            self.isLeaf = False

        def getIndexCount(self):
            count = 0
            index = -1

            for i in range(len(self.childs)):
                if self.childs[i]:
                    count += 1
                    index = i
            return (count, index)

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode()

    def convertIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        length = len(word)

        for level in range(length):
            ch = word[level]
            index = self.convertIndex(ch)
            if not root.childs[index]:
                root.childs[index] = self.TrieNode()
            root = root.childs[index]
        root.isLeaf = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for ch in word:
            index = self.convertIndex(ch)
            if not root.childs[index]:
                return False
            root = root.childs[index]

        return True and root.isLeaf

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for ch in prefix:
            index = self.convertIndex(ch)
            if not root.childs[index]:
                return False
            root = root.childs[index]
        return True
