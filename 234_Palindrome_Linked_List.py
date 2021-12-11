'''
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
'''

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        def recursivePalindrome(node):
            nonlocal frontNode
            if node is not None:
                if not recursivePalindrome(node.next): return False
                if frontNode.val != node.val: return False
                frontNode = frontNode.next
            return True

        frontNode = head
        return recursivePalindrome(head)

    #         curr = head
    #         N, stack = 0, []

    #         while curr:
    #             N+=1
    #             curr = curr.next
    #         if N == 0: return False
    #         if N == 1: return True

    #         mid = (N//2)+1
    #         curr = head
    #         i = 1
    #         while curr:
    #             if i >= mid: break
    #             stack.append(curr.val)
    #             curr = curr.next
    #             i+=1
    #         if N%2 == 1: curr = curr.next
    #         while curr:
    #             item = stack.pop()
    #             if item != curr.val: return False
    #             curr = curr.next

    #         return True