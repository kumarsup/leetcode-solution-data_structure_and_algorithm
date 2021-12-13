'''
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].



Example 1:


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
Example 3:

Input: firstList = [], secondList = [[4,8],[10,12]]
Output: []
Example 4:

Input: firstList = [[1,7]], secondList = [[3,10]]
Output: [[3,7]]


Constraints:

0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109
endj < startj+1
'''


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstLen, firstP, secondLen, secondP, start, end, res = len(firstList), 0, len(secondList), 0, 0, 0, []

        def isIntersect(first, second):
            maxStart = max(first[0], second[0])
            minEnd = min(first[1], second[1])
            return (maxStart <= second[1] and maxStart <= first[1] and minEnd >= second[0] and minEnd >= first[0])

        while firstP < firstLen and secondP < secondLen:
            if isIntersect(firstList[firstP], secondList[secondP]):
                start = max(firstList[firstP][0], secondList[secondP][0])
                end = min(firstList[firstP][1], secondList[secondP][1])
                res.append([start, end])

            if firstList[firstP][1] == secondList[secondP][1]:
                firstP += 1
                secondP += 1
            elif firstList[firstP][1] < secondList[secondP][1]:
                firstP += 1
            else:
                secondP += 1
        return res




