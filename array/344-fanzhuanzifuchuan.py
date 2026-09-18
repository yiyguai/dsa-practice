#344.反转字符串
#双指针，当快指针减慢指针小于等于1时，说明已经交换完毕

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        k = j = 0
        if len(s) > 1:
            for i in range(len(s)-1,-1,-1):
                k = s[i]
                s[i] = s[j]
                s[j] = k
                j += 1
                if i-j<=1:
                    break