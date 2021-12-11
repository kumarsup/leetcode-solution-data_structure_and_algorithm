'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's
strstr() and Java's indexOf().

 Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0

Constraints:
0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if needle == '': return 0
        if needle == haystack: return 0
        if len(needle) == 0: return 0
        if len(needle) > len(haystack): return -1

        x = len(haystack)
        l = len(needle)
        if haystack == needle:
            return 0
        if x == 0 and l == 0:
            return 0
        for i in range(0, x - l + 1):
            if haystack[i:i + l] == needle:
                return i
        return -1