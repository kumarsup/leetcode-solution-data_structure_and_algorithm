class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1
        left, maxLen, hm = 0, 0, {}
        for right in range(len(s)):
            if s[right] in hm:
                left = max(hm[s[right]], left)
            maxLen = max(maxLen, right-left + 1)
            hm[s[right]] = right + 1
        return maxLen