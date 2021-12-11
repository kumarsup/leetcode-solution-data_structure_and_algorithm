'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence
of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #         N = len(s)
        #         word_set = set(wordDict)
        #         dp = [False]*(N+1)
        #         dp[0] = True

        #         for i in range(1, N+1):
        #             for j in range(i):
        #                 if dp[j] and s[j:i] in word_set:
        #                     dp[i] = True
        #                     break
        #         return dp[N]

        N = len(s)
        dp = [None] * (N + 1)

        def backTrack(start):
            if start == N: return True
            if dp[start] is not None: return dp[start]
            for end in range(start + 1, N + 1):
                if s[start:end] in wordDict:
                    dp[start] = backTrack(end)
                    if dp[start]: return True
            return False

        return backTrack(0)