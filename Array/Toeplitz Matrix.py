#coding=u8

"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
"""

class Solution(object):
    def isToeplitzMatrix1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row_num = len(matrix)
        col_num = len(matrix[0])

        for i in range(row_num - 1):
            for j in range(col_num - 1):
                if matrix[i][j] == matrix[i + 1][j + 1]:
                    continue
                else:
                    return False
        return True

    def isToeplitzMatrix2(self,matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all([matrix[i][j] == matrix[i+1][j+1] for j in range(len(matrix[0])-1) for i in range(len(matrix)-1) ])

matrix=[[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(Solution().isToeplitzMatrix2(matrix))

