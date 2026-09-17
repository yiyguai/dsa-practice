#283. 移动零
#双指针，快指针确定非零数并由慢指针记录，一次遍历后，补上末尾的0即可

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        if len(nums) > 1:
            for j in range(0,len(nums)):
                if nums[j] != 0:
                    nums[i] = nums[j]
                    i += 1
            for k in range(i,len(nums)):
                nums[k] = 0
            return nums
        else:
            return nums