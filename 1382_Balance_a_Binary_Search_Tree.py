'''
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.



Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]


Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
'''


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root: return root
        arr = []

        def dfs(node):
            if not node: return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)

        # print(arr)
        # iterate on this array and construct a BST

        def constructBSTTree(arr):
            if len(arr) <= 0: return None
            l, r = 0, len(arr) - 1
            if l > r: return None

            mid = (l + r) // 2
            root = TreeNode(arr[mid])
            root.left = constructBSTTree(arr[l:mid])
            root.right = constructBSTTree(arr[mid + 1:r + 1])
            return root

        return constructBSTTree(arr)