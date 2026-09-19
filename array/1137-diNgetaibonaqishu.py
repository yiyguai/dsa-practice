#1137.第n个泰波那契数
#第n个泰波那契数由第n-1个、第n-2个和第n-3个泰波那契数的和组成

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = p = 0
        r = s = 1
        if n == 0:
            return 0
        elif n < 3:
            return 1
        else:
            while n-2 != 0:
                d = p
                p = r
                r = s
                s = d + p + r
                n -= 1
            return s