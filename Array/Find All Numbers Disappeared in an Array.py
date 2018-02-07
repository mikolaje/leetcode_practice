class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        all_set = set(range(1, len(nums) + 1))
        existed_set = set(nums)
        ret = all_set - existed_set
        return list(ret)