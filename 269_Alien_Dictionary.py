'''
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted
lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the
new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s
comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is
smaller if and only if s.length < t.length.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
'''


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {char: [] for word in words for char in word}
        for first, second in zip(words, words[1:]):
            for c, d in zip(first, second):
                if c != d:
                    graph[d].append(c)
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second) < len(first):
                    return ""

        def DFS(curr, output, seen):
            if curr in seen: return seen[curr]
            seen[curr] = False
            for node in graph[curr]:
                res = DFS(node, output, seen)
                if not res: return res
            seen[curr] = True
            output.append(curr)
            return True

        output, seen = [], {}
        for i in graph:
            if not DFS(i, output, seen):
                return ""
        return "".join(output)