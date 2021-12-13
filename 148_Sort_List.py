'''
Given the head of a linked list, return the list after sorting it in ascending order.



Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
'''


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return head

        def findMid(curr):
            if not curr: return curr
            prev = None
            while curr and curr.next:
                prev = prev.next if prev is not None else curr
                curr = curr.next.next

            mid = prev.next
            prev.next = None
            return mid

        def merge(node1, node2):

            dummyHead = ListNode(-1)
            tail = dummyHead

            while node1 and node2:
                if node1.val < node2.val:
                    tail.next = node1
                    node1 = node1.next
                    tail = tail.next
                else:
                    tail.next = node2
                    node2 = node2.next
                    tail = tail.next

            tail.next = node1 if node1 else node2
            return dummyHead.next

        def mergeSort(node):
            if not node or not node.next: return node
            mid = findMid(node)
            # print(mid.val)
            left = mergeSort(node)
            right = mergeSort(mid)
            return merge(left, right)

        return mergeSort(head)
