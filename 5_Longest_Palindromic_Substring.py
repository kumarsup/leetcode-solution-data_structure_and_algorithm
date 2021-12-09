'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0: return ""
        res, maxLength, N = s[0], 0, len(s)

        def getPalindrome(start, end):
            nonlocal res
            while start >= 0 and end < N and s[start] == s[end]:
                if len(res) < end - start + 1:
                    res = s[start:end + 1]
                start, end = start - 1, end + 1

        for i in range(0, N):
            start = end = i
            while start >= 0 and end < N and s[start] == s[end]:
                if len(res) < end - start + 1:
                    res = s[start:end + 1]
                start, end = start - 1, end + 1

            start, end = i, i + 1
            while start >= 0 and end < N and s[start] == s[end]:
                if len(res) < end - start + 1:
                    res = s[start:end + 1]
                start, end = start - 1, end + 1
        return res

#         def longestPalindromeR(start, end):
#             if start > end: return 0
#             if start == end: return 1

#             if s[start] == s[end]:
#                 remLength = end - start - 1
#                 if remLength == longestPalindromeR(start+1, end-1):
#                     return remLength + 2
#             c1 = longestPalindromeR(start+1, end)
#             c2 = longestPalindromeR(start, end-1)
#             print(start, end)
#             return max(c1, c2)

#         return longestPalindromeR(0, len(s)-1)


#         def longestPalindromeR(start, end):
#             if start > end: return 0
#             if start == end: return 1

#             if s[start] == s[end]:
#                 remLength = end - start - 1
#                 if remLength == longestPalindromeR(start+1, end-1):
#                     return remLength + 2
#             c1 = longestPalindromeR(start+1, end)
#             c2 = longestPalindromeR(start, end-1)
#             print(start, end)
#             return max(c1, c2)

#         return longestPalindromeR(0, len(s)-1)