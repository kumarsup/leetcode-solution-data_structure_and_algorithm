'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of
them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct
course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
'''


class Solution:

    #     def topologicalSortUtils(self, graph, visitSet, vertex, stack):
    #         if vertex in visitSet: return
    #         visitSet.add(vertex)

    #         for i in graph[vertex]:
    #             if i not in visitSet:
    #                 self.topologicalSortUtils(graph, visitSet, i, stack)
    #         stack.append(vertex)

    #     def topologicalSort(self, graph, vertex):
    #         visitSet = set()
    #         stack = []
    #         for i in graph:
    #             if i not in visitSet:
    #                 self.topologicalSortUtils(graph, visitSet, i, stack)
    #         return stack

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        inDegree = {i: 0 for i in range(numCourses)}

        for cource, pre in prerequisites:
            graph[cource].append(pre)
            inDegree[pre] += 1

        queue = [i for i in range(numCourses) if not inDegree[i]]
        # print(inDegree)
        # print(queue)

        seen = set(queue)
        res = []

        for course in queue:
            res.insert(0, course)
            for pre in graph[course]:
                if pre in seen:
                    return []
                inDegree[pre] -= 1

                if not inDegree[pre]:
                    queue.append(pre)
                    seen.add(pre)
        return res if len(seen) == numCourses else []
