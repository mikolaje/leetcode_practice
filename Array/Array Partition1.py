#coding=u8

"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
"""

class Solution():
    def arrayPairSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = []
        nums = sorted(nums)
        for i in range(0,len(nums),2):
            m = min(nums[i],nums[i+1])
            l.append(m)

        return sum(l)

    def arrayPairSum2(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])


print(Solution().arrayPairSum2([3,2,4,1]))