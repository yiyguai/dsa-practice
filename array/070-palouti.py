#070.爬楼梯
#第n阶楼梯由第n-1阶楼梯上爬1阶和第n-2阶楼梯上爬2阶组成，两种方法的总和就是第n阶楼梯的总方法数

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = j =0
        k = 1
        while n != 0:
            i = j
            j = k
            k = i + j
            n -= 1
        return k