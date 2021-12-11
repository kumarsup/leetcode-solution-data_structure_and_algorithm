'''
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100


Follow up: Can you flatten the tree in-place (with O(1) extra space)?
'''


class Solution:
    def flatten(self, root: TreeNode) -> None:
        head = None
        curr = None

        def dfs(node):
            nonlocal curr, head
            if not node: return None

            if not node.left and not node.right: return node
            left = dfs(node.left)
            right = dfs(node.right)

            if left:
                left.right = node.right
                node.right = node.left
                node.left = None

            return right if right else left

        dfs(root)