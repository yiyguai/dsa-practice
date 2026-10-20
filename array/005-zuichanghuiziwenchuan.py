#005-最长回文子串
#使用单指针遍历数组，res更新最长回文子串，用倒序是否与正序相同做判断

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        for i in range(len(s)):
            start = max(i-len(res)-1,0)
            temp = s[start:i+1]
            if temp == temp[::-1]:
                res = temp
            else:
                temp = temp[1:]
                if temp == temp[::-1]:
                    res = temp
        return res