#coding=u8

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        _len = len(nums)
        for i in nums:
            count = dic.get(i, 0) + 1
            dic[i] = count

        for k, v in dic.iteritems():  # 用iteritems貌似可以节省点时间
            if v > _len / 2:
                return k