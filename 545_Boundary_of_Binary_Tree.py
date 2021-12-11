'''
The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
If a node in the left boundary and has a left child, then the left child is in the left boundary.
If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again,
the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.

Example 1:
Input: root = [1,null,2,3,4]
Output: [1,3,4,2]
Explanation:
- The left boundary is empty because the root does not have a left child.
- The right boundary follows the path starting from the root's right child 2 -> 4.
  4 is a leaf, so the right boundary is [2].
- The leaves from left to right are [3,4].
Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].

Example 2:
Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
Output: [1,2,4,7,8,9,10,6,3]
Explanation:
- The left boundary follows the path starting from the root's left child 2 -> 4.
  4 is a leaf, so the left boundary is [2].
- The right boundary follows the path starting from the root's right child 3 -> 6 -> 10.
  10 is a leaf, so the right boundary is [3,6], and in reverse order is [6,3].
- The leaves from left to right are [4,7,8,9,10].
Concatenating everything results in [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3].

Constraints:
The number of nodes in the tree is in the range [1, 104].
-1000 <= Node.val <= 1000
'''
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        if not root.left and not root.right: return [root.val]
        left, right, leaf = [], [], []

        def get_leafs(node, leaf):
            if not node: return
            if not node.left and not node.right: leaf.append(node.val)
            get_leafs(node.left, leaf)
            get_leafs(node.right, leaf)

        def get_left_bound(node, left):
            if not node or (not node.left and not node.right): return
            left.append(node.val)
            if not node.left and node.right:
                get_left_bound(node.right, left)
            else:
                get_left_bound(node.left, left)

        def get_right_bound(node, right):
            if not node or (not node.left and not node.right): return
            right.append(node.val)
            if not node.right and node.left:
                get_right_bound(node.left, right)
            else:
                get_right_bound(node.right, right)

        get_leafs(root, leaf)
        get_left_bound(root.left, left)
        get_right_bound(root.right, right)

        # print(left, leaf, right[::-1])

        return [root.val] + left + leaf + right[::-1]

#         if not root: return []
#         left, right, leaf = [], [], []
#         mapping = defaultdict(int)
#         res, queue = [], deque([root])
#         position = 0
#         def checkAndAdd(arr, val, pos = -1):
#             if val not in right and val not in left and val not in leaf:
#                 if pos != -1: arr.insert(pos, val)
#                 else: arr.append(val)

#         while queue:
#             if mapping[queue[0].val] == 0:
#                 checkAndAdd(left, queue[0].val)
#             else:
#                 checkAndAdd(right, queue[0].val, position)
#                 position+=1

#             checkAndAdd(right, queue[-1].val, position)

#             for i in range(len(queue)):
#                 node = queue.popleft()
#                 if node and node.left:
#                     queue.append(node.left)
#                     mapping[node.left.val] = 0
#                 if node and node.right:
#                     queue.append(node.right)
#                     mapping[node.right.val] = 1
#                 if not node.left and not node.right:
#                     checkAndAdd(leaf, node.val)
#         print(left,"---", leaf, "---", right)
#         return left + leaf + right