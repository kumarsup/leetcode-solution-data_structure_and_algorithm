'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
'''


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        minHeap, count = [], 0
        for node in lists:
            if node:
                heapq.heappush(minHeap, (node.val, count, node))
                count += 1

        head, tail = None, None
        while minHeap:
            item = heapq.heappop(minHeap)
            node = item[2]
            if head is None:
                head, tail = node, node
            else:
                tail.next = node
                tail = tail.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, count, node.next))
                count += 1

        return head