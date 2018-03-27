# coding=u8

class Solution():
    def twoSum1(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 刚开始用的是这种方法，但是这个时间复杂度是O(n*n)
        _len = len(nums)
        for i in range(_len):
            for j in range(i+1,_len):
                if nums[i] + nums[j] == target:
                    return [i,j]


    def twoSum2(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup={}   # dict 的key为num的另一半； value 为num的index
        for i,element in enumerate(nums):
            if target-element in lookup:
                return [lookup[target-element],i]
            else:
                lookup[element] = i

print(Solution().twoSum2([3,2,3],6))