'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True

        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                j = n - 1 - i
                return is_palindrome(i, j - 1) or is_palindrome(i + 1, j)
        return True