'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.

'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        # Without DP
        # count, N = len(s), len(s)
        # dp = [[False]*N for _ in range(N)]
        # for i in range(N): dp[i][i] = True
        # for start in range(N-1, -1, -1):
        #     for end in range(start+1, N):
        #         if s[start] == s[end]:
        #             if end - start == 1 or dp[start+1][end-1]:
        #                 dp[start][end] = True
        #                 count+=1
        # return count

        # Without DP
        count, N = 0, len(s)

        def countPalindrome(start, end):
            nonlocal count, N
            while start >= 0 and end < N and s[start] == s[end]:
                start, end = start - 1, end + 1
                count += 1

        for i in range(N):
            countPalindrome(i, i)
            countPalindrome(i, i + 1)
        return count