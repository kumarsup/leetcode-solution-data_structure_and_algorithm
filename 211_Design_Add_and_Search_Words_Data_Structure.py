'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
'''


class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.eow = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.child[ch]
        node.eow = True

    def searchWord(self, word, root, count=0) -> bool:
        node = root

        if count == len(word):
            return node.eow

        if word[count] is ".":
            for k in node.child:
                found = self.searchWord(word, node.child[k], count + 1)
                if found:
                    return found
        else:
            if word[count] not in node.child:
                return False
            return self.searchWord(word, node.child[word[count]], count + 1)

        return False

    # ".ad" --- > "b,a,d- d,a,d"
    def search(self, word: str) -> bool:
        res = False
        return self.searchWord(word, self.root)
