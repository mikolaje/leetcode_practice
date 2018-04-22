# coding=u8
class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        _len = len(prices)

        for i in range(_len):
            for j in range(i + 1, _len):
                max_profit = max(prices[j] - prices[i], max_profit)

        return max_profit

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        min_price = float('inf')  # 表示无穷大
        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)
        return profit

