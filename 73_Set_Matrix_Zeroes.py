'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.



Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        colsArr = [False] * cols
        rowsArr = [False] * rows

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowsArr[i] = True
                    colsArr[j] = True

        for i in range(len(rowsArr)):
            if rowsArr[i] is True:
                for j in range(cols):
                    matrix[i][j] = 0

        for i in range(len(colsArr)):
            if colsArr[i] is True:
                for j in range(rows):
                    matrix[j][i] = 0