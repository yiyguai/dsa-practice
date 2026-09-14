# 1. Two Sum / 两数之和
# 链接: https://leetcode.cn/problems/two-sum/
# 思路: 遍历列表，并通过相减确认另一个值，判断这个值是否在列表中，若存在则返回索引
# 复杂度: 时间 O( ) / 空间 O( )
# 易错点:

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums[i+1:]:
                return [i,nums[i+1:].index(res)+i+1]
        pass