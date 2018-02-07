#coding=u8

"""

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""

class Solution(object):
    def matrixReshape1(self, nums, r, c):

        # 很笨的方法。第一次想的。呵呵
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        rows = len(nums)
        cols = len(nums[0])

        if r*c != rows*cols:
            return nums
        else:
            l = []
            for each in nums:
                l.extend(each)
            print(l)
            a=[]
            final=[]
            for i,each in enumerate(l):
                a.append(each)
                if (i+1)%c==0:
                    final.append(a)
                    a=[]

            return final

    def matrixReshape2(self,nums,r,c):
        #http://stupidpythonideas.blogspot.de/2013/08/how-grouper-works.html
        flat = sum(nums, [])     #相当于[]+[1,2]+[3,4]
        if len(flat) != r * c:
            return nums
        tuples = zip(*([iter(flat)] * c))  # 这里还是比较有趣的。
        result = map(list,tuples)
        return list(result)

print(Solution().matrixReshape2([[1,2],[3,4]],1,4))

