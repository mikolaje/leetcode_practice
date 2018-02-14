#coding=u8

"""
思路：用递归的思想
dp(n): min cost to climb to n-th step

dp(n) = min(dp(n-1)+cost[n-1],
            dp(n-2)+cost[n-2])
ans=arr(n)

https://www.youtube.com/watch?v=v3WqNLmmBdk
"""


class Solution(object):

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        _len = len(cost)
        dp = [0] * _len
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, _len):
            dp[i] = min(dp[i-2] + cost[i], dp[i-1] + cost[i])

        return min(dp[-1], dp[-2])

print(Solution().minCostClimbingStairs([1, 2, 3]))
