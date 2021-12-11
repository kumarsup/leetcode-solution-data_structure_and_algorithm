'''
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.



Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.


Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50

'''


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0: return 0
        if n == 1: return 1 if k != 0 else k

        left, right, maxLen, mm = 0, 0, 0, {}

        while left <= right and right < n:
            if s[right] not in mm:
                mm[s[right]] = 0
            mm[s[right]] += 1

            if len(mm) > k:
                mm[s[left]] -= 1
                if mm[s[left]] == 0: del mm[s[left]]
                left += 1
            right += 1
            maxLen = max(maxLen, right - left)
            # print(mm, left, right)
        return maxLen