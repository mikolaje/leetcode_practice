# coding=u8


class Solution(object):
    def searchInsert1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target == nums[i]:
                return i

            if target<nums[i]:
                return i
        return len(nums)

    def searchInsert2(self,nums,target):
        return len([x for x in range(nums) if target>x])
