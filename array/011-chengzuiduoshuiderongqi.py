#11.盛最多水的容器
#双指针，短的一端决定容量，移动短的一端可能获得更大的容量，比较容量大小
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = j = n = m = 0
        k = len(height)-1
        while k != j:
            if height[j] < height[k]:
                n = height[j]
                m = (k-j)*n
                j += 1
            else:
                n = height[k]
                m = (k-j)*n
                k -= 1
            if m > i:
                i = m
            else:
                continue
        return i