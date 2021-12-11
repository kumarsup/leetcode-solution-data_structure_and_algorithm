'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for i in reversed(range(M)):
            for j in reversed(range(N)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]

    #         M, N = len(text1), len(text2)
    #         dp = [[None]*N for _ in range(M)]
    #         def findLCS(i, j):
    #             nonlocal M, N
    #             if i >= M or j >= N: return 0
    #             if dp[i][j] is not None: return dp[i][j]
    #             if text1[i] == text2[j]: return 1 + findLCS(i+1, j+1)
    #             dp[i][j] = max(findLCS(i+1, j), findLCS(i, j+1))
    #             return dp[i][j]
    #         return findLCS(0, 0)