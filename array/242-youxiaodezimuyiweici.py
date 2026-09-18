#242.有效的字母异位词
#使用Counter计数器

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        k = Counter()
        for i in s:
            k[i] += 1
        for j in t:
            k[j] -=1
            if k[j] == 0:
                del k[j]
        return True if len(k) == 0 else False