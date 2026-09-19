#746.使用最小花费爬楼梯
#第i阶楼梯的最小花费由第i-1阶和第i-2阶楼梯的最小花费决定

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) < 2:
            return 0
        else:
            p = d = i = r = 0
            while i+1 != len(cost):
                p = d
                d = r
                if p + cost[i] > d + cost[i+1]:
                    r = d + cost[i+1] 
                else:
                    r = p + cost[i]
                i += 1
            return r