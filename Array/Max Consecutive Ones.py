#coding=u8
"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""


class Solution(object):
    def findMaxConsecutiveOnes1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        l=[]
        for i in nums:
            if i==1:
                counter +=1
            else:
                l.append(counter)
                counter = 0
        l.append(counter)
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        else:
            return max(l)

    def findMaxConsecutiveOnes2(self,nums):
        counter = 0
        final_result = 0
        for i in nums:
            if i == 1:
                counter += 1
            else:
                final_result=max(counter,final_result)
                counter = 0
        final_result = max(counter, final_result)

        return final_result