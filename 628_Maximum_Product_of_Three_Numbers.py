'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.



Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6


Constraints:

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000

'''
from functools import reduce


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        minHeap = []  # store max 3 number from array
        minNegHeap = []  # store min 2 number from array

        for num in nums:

            if len(minHeap) < 3:
                heapq.heappush(minHeap, num)
            else:
                heapq.heappush(minHeap, num)
                heapq.heappop(minHeap)

            if num < 0:
                if len(minNegHeap) < 2:
                    heapq.heappush(minNegHeap, -num)
                else:
                    heapq.heappush(minNegHeap, -num)
                    heapq.heappop(minNegHeap)

        result = reduce((lambda x, y: x * y), minHeap)
        if len(minNegHeap) == 2:
            result2 = reduce((lambda x, y: -x * -y), minNegHeap)
            result = max(result, result2 * max(minHeap))
        return result