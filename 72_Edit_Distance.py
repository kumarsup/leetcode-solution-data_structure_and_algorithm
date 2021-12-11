'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''


class Solution:
    def minDistance(self, s: str, t: str) -> int:
        ns, nt = len(s), len(t)
        if not ns * nt: return ns + nt
        dp = [[0] * (nt + 1) for _ in range(ns + 1)]
        for i in range(ns + 1): dp[i][0] = i
        for i in range(nt + 1): dp[0][i] = i

        for i in range(1, ns + 1):
            for j in range(1, nt + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1] - 1)
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
        return dp[ns][nt]
