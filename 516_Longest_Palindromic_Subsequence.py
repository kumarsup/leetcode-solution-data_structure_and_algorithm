'''
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".


Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
'''


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[None] * n for _ in range(n)]

        def recursive(start, end):
            nonlocal dp
            if start > end: return 0
            if start == end: return 1
            if dp[start][end] is not None: return dp[start][end]
            if s[start] == s[end]: return 2 + recursive(start + 1, end - 1)
            c1 = recursive(start + 1, end)
            c2 = recursive(start, end - 1)
            dp[start][end] = max(c1, c2)
            return dp[start][end]

        return recursive(0, n - 1)

