'''
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction,
then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

Example 1:
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]

Example 2:
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

Constraints:
-300 <= x, y <= 300
0 <= |x| + |y| <= 300
'''


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        MOVES = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        def BFS(x, y):
            visited = set()
            queue = deque([(0, 0)])
            steps = 0

            while queue:
                curr_level_cnt = len(queue)
                for i in range(curr_level_cnt):
                    curr_x, curr_y = queue.popleft()
                    if (curr_x, curr_y) == (x, y):
                        return steps

                    for offset_x, offset_y in MOVES:
                        next_x, next_y = curr_x + offset_x, curr_y + offset_y

                        if (next_x, next_y) not in visited:
                            visited.add((next_x, next_y))
                            queue.append((next_x, next_y))
                steps += 1

        return BFS(x, y)

#         def get_neighbours(node):
#             x, y = node
#             neighbours = set()
#             for move in MOVES:
#                 xx = x+move[0]
#                 yy = y+move[1]
#                 if 0 <= xx < sys.maxsize  and 0 <= yy < sys.maxsize:
#                     neighbours.add((xx, yy))
#             return neighbours

#         def backTrack(src, dest, visited, count):
#             if src in visited:
#                 return False

#             visited.add(src)

#             #print(src, dest)
#             if src[0] == dest[0] and src[1] == dest[1]:
#                 print("found- HAHAH", count)
#                 return True
#             count = count+1
#             neighbours = get_neighbours(src)
#             for nei in neighbours:
#                 val = backTrack(nei, dest, visited, count)
#                 if val:
#                     print("FOUND count",count)
#                     return
#             return False

#         visited = set()
#         return backTrack((0,0), (x, y), visited, 0)
