'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''


class Solution:
    class Trie:
        class TrieNode:
            def __init__(self):
                self.childs = [None] * 26
                self.isLeaf = False

            def getOneChildIndex(self):
                count = 0
                global indexs
                for i in range(len(self.childs)):
                    if self.childs[i]:
                        count += 1
                        indexs = i
                        if count > 1: return -1
                return count

        def __init__(self):
            self.root = self.TrieNode()

        def getNode(self):
            return self.TrieNode()

        def convertIndex(self, ch):
            return ord(ch) - ord('a')

        def insert(self, key):
            root = self.root
            length = len(key)

            for level in range(length):
                ch = key[level]
                index = self.convertIndex(ch)
                if not root.childs[index]:
                    root.childs[index] = self.getNode()
                root = root.childs[index]
            root.isLeaf = True

        def prefix(self):
            root = self.root
            prefix = ""
            while root.getOneChildIndex() == 1 and root.isLeaf == False:
                prefix += chr(97 + indexs)
                root = root.childs[indexs]
            return prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = self.Trie()
        for word in strs:
            if word is "": return ""
            trie.insert(word)
        return trie.prefix()