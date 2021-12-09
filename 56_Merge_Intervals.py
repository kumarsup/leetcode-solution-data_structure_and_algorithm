class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        n, res = len(intervals), []
        intervals.sort(key=lambda x: x[0])
        last = intervals[0]
        for i in range(1, n):
            curr = intervals[i]
            if last[1] >= curr[0]:
                last[1] = max(last[1], curr[1])
            else:
                res.append(last)
                last = curr
        res.append(last)
        return res