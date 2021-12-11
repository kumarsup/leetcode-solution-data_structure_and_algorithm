'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result
should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:
1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
'''


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]

#         heap = []

#         for item in arr:
#             diff = -abs(item-x)
#             if len(heap) < k:
#                 heapq.heappush(heap, (diff, item))
#             else:
#                 if diff > heap[0][0]:
#                     heapq.heappush(heap, (diff, item))
#                     heapq.heappop(heap)
#         return sorted([item[1] for item in heap])