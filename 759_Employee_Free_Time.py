'''
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays.
For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't
include intervals like [5, 5] in our answer, as they have zero length.

Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.

Example 2:
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]

Constraints:
1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8
'''


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        N, A = len(schedule), schedule
        intervals, res, heap = [], [], []

        for inter in range(N):
            item = A[inter]
            for i in range(len(item)):
                intervals.append([item[i].start, item[i].end])
        intervals.sort(key=lambda x: x[0])
        last = intervals[0]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if last[1] > curr[0]:
                last[1] = max(last[1], curr[1])
            else:
                heapq.heappush(heap, (last[0], last[1]))
                last = curr
        heapq.heappush(heap, (last[0], last[1]))

        while heap:
            start, end = heapq.heappop(heap)
            if heap:
                start_top, end_top = heap[0]
                if start_top >= end and end_top > end and end != start_top:
                    res.append(Interval(end, start_top))
        return res