class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for index,value in enumerate(nums):
            hash_map[value]=index
        for index1,value in enumerate(nums):
            if (target-value) in hash_map:
                pass

s=Solution()
s.twoSum([1,2,3,43,5,45],48)