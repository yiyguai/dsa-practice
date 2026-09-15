#27. Remove Element/移除元素
#思路：双指针，一个指向当前要放置的元素位置，另一个遍历数组 
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j