# coding=u8

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 这方法提交没成功
        for i in range(len(nums)):
            while nums[i] == 0:  # 这里要用while不能用if 因为如果满足这个条件要再重复下面这步操作
                nums.append(nums.pop(i))

            print(nums)

    def moveZeroes2(self, nums):
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        print(nums)

print(Solution().moveZeroes2([0, 0, 1]))