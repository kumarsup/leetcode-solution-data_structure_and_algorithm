'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of
all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:
Input: root = [1], target = 1, k = 3
Output: []

Constraints:
The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
'''


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        ans = []

        # Return distance from node to target if exists, else -1
        # Vertex distance: the # of vertices on the path from node to target
        def dfs(node):
            if not node:
                return -1
            elif node is target:
                subtree_add(node, 0)
                return 1
            else:
                L, R = dfs(node.left), dfs(node.right)
                if L != -1:
                    if L == K: ans.append(node.val)
                    subtree_add(node.right, L + 1)
                    return L + 1
                elif R != -1:
                    if R == K: ans.append(node.val)
                    subtree_add(node.left, R + 1)
                    return R + 1
                else:
                    return -1

        # Add all nodes 'K - dist' from the node to answer.
        def subtree_add(node, dist):
            if not node:
                return
            elif dist == K:
                ans.append(node.val)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)

        dfs(root)
        return ans

#         distance = defaultdict(list)
#         targetData = (0, None)
#         distance[targetData] = [root.val]

#         def dfs(node, d, left):
#             nonlocal distance, targetData
#             if not node: return False
#             if node.val == target.val:
#                 targetData = (d, left)
#             distance[(d, left)].append(node.val)

#             dfs(node.left, d+1, left)
#             dfs(node.right, d+1, left)

#         dfs(root.left, 1, True)
#         dfs(root.right, 1, False)

#         targetD = targetData[0]
#         targetSubTree = targetData[1]
#         print(distance, k, targetD)

#         if not targetSubTree:
#             return distance[(k, False)]+distance[(k, True)]
#         elif targetSubTree:
#             return distance[(targetD-k, None)] + distance[(targetD+k, True)]+distance[(targetD-k, True)] + distance[(k-targetD, False)]
#         else:
#             return distance[(targetD-k, None)] + distance[(targetD+k, False)]+distance[(targetD-k, False)] + distance[(k-targetD, True)]
