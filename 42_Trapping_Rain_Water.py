class Solution:
    def trap(self, heights: List[int]) -> int:
        leftMax, rightMax, N, area, dp = 0, 0, len(heights), 0, [0] * len(heights)

        for i in range(len(heights) - 1, -1, -1):
            rightMax = max(rightMax, heights[i])
            dp[i] = rightMax

        for i in range(N):
            leftMax, rightMax = max(leftMax, heights[i]), dp[i]
            diff = min(leftMax, rightMax)
            if heights[i] < diff:
                area += diff - heights[i]
        return area