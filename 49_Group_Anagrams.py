'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n, mm = len(strs), {}

        def generate_key(word):
            hashVal = 0
            for ch in word:
                hashVal += hash(ch)
            return hashVal

        for i in range(n):
            word = strs[i]
            key = generate_key(word)
            if key not in mm:
                mm[key] = []
            mm[key].append(word)
        return mm.values()