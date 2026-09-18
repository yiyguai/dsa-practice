#217.找出重复元素
#转成集合后比较长度

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums))!=len(nums)