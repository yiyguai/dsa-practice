#509.斐波那契数
#第n个斐波那契数由第n-1个和第n-2个斐波那契数的和组成

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        p = d = 0
        r = 1
        while n-1 != 0:
            p = d
            d = r
            r = p + d
            n -= 1
        return r 