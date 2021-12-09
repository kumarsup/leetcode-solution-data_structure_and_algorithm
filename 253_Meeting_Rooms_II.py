'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:
1 <= intervals.length <= 104
0 <= starti < endi <= 106
'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2: return len(intervals)
        intervals.sort(key=lambda x: x[0])

        count, heap = 1, [intervals[0][1]]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            while len(heap) > 0 and heap[0] <= curr[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, curr[1])
            count = max(count, len(heap))
            print(heap)
        return count
