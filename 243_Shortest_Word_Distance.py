'''
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.



Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1


Constraints:

1 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
'''


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        minDist, index1, index2, n = float('inf'), -1, -1, len(wordsDict)

        for i in range(n):
            if word1 == wordsDict[i]:
                index1 = i
            elif word2 == wordsDict[i]:
                index2 = i

            if index1 != -1 and index2 != -1:
                minDist = min(minDist, abs(index1 - index2))
        return minDist