'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.



Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words: return []
        if len(words) <= 1: return []
        counter = Counter(words[0])

        for i in range(1, len(words)):
            word = words[i]
            temp = Counter(word)
            for key in list(counter.keys()):
                if key not in temp:
                    del counter[key]
                else:
                    counter[key] = min(counter[key], temp[key])

        res = []

        for k, v in counter.items():
            res += k * v

        return res