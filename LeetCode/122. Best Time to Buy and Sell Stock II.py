#-*-coding:utf-8 -*-
"""
    122. Best Time to Buy and Sell Stock II
    Directed by user zhongch4g
    current system date 2017/4/17
"""

class Solution(object):
    # # def maxProfit(self, prices):
    # """
    # :type prices: List[int]
    # :rtype: int
    # """
    # max_profit = 0
    # if prices is [] or prices is None:
    #     return max_prices
    # for index in range(len(prices) - 1):
    #     if prices[index + 1] > prices[index]:
    #         max_profit = max_profit + (prices[index + 1] - prices[index])
    # return max_profit

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if prices is [] or prices is None:
            return max_profit
        judge = []
        for index in range(len(prices) - 1):
            if (prices[index + 1] - prices[index]) > 0:
                judge.append(True)
            else:
                judge.append(False)
        for jud in range(len(judge)):
            if(judge[jud] is True):
                max_profit = max_profit + (prices[jud + 1] - prices[jud])
        return max_profit



# stock_prices = [7, 5, 4, 3, 1]
# stock_prices = [1, 5, 2, 7, 9]
stock_prices = [1, 2, 1, 100] #ith element means day i price
instance = Solution()
instance.maxProfit(stock_prices)
