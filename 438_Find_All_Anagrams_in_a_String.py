'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
'''


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter()

        output = []
        # sliding window on the string s
        for i in range(ns):
            s_count[s[i]] += 1
            if i >= np:
                s_count[s[i - np]] -= 1
                if s_count[s[i - np]] == 0: del s_count[s[i - np]]
            if p_count == s_count: output.append(i - np + 1)
        return output

#         sn = len(s)
#         pn = len(p)
#         hm={}

#         for x in p:
#             if x not in hm: hm[x] = 0
#             hm[x] += 1

#         def validate(val, hmap):
#             for x in val:
#                 if x not in hmap or hmap[x] == 0: return False
#                 hmap[x]-=1
#             return True

#         left, res = 0, []

#         for i in range(sn):
#             if pn <= i-left+1:
#                 if validate(s[left:i+1], hm.copy()):
#                     res.append(left)
#                 left+=1
#         return res