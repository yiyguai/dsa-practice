# 26. Remove Duplicates from Sorted Array / 删除有序数组中的重复项
# 链接: https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
# 思路:
# 复杂度: 时间 O( ) / 空间 O( )
# 易错点:

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
        pass
