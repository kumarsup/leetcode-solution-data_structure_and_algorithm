'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''
class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        ns, np = len(s), len(p)
        if ns < np: return []
        p_count, s_count, output = Counter(p), Counter(), []
        for i in range(ns):
            s_count[s[i]] += 1
            if i >= np:
                s_count[s[i - np]] -= 1
                if s_count[s[i - np]] == 0: del s_count[s[i - np]]
            if p_count == s_count: output.append(i - np + 1)
        return output