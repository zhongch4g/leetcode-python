#-*-coding:utf-8 -*-
"""
    121. Best Time to Buy and Sell Stock
    Directed by user zhongch4g
    current system date 2017/4/29
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # 题目意思表述不清晰，正确的题目含义是只允许交易一次
        # getMoney = 0
        # setGoal = 0
        # for i in range(1, len(prices)):
        #     j = i - 1
        #     # print i, j
        #     if prices[j] > prices[i]:
        #         continue
        #     else:
        #         setGoal = j
        #         break
        # goal = setGoal
        # for k in range(goal + 1, len(prices)):
        #     if prices[k] > prices[setGoal]:
        #         getMoney = getMoney + prices[k] - prices[setGoal]
        #         setGoal = k
        #     else:
        #         setGoal = k
        # return getMoney

        # 找到list中的最大最小，求两数相减后除以2，然后list中每个元素减去得到的数
        # if not prices:
        #     return 0
        # maxlist = max(prices)
        # minlist = min(prices)
        # sub = (maxlist - minlist)/2.0
        # # print sub
        # flag = 0
        # for i in range(len(prices)):
        #     prices[i] = prices[i] - sub
        #     if prices[i] < 0:
        #         flag = 1
        # if flag == 0:
        #     return int(max(prices) - min(prices))
        # # print prices
        # maxprofit = 0
        # for i in range(len(prices)):
        #     if prices[i] <= 0 and maxprofit < (max(prices[i:]) - prices[i]):
        #         maxprofit = max(prices[i:]) - prices[i]
        # # if maxprofit == 0:
        # #     maxprofit = max(prices) - min(prices)
        # return int(maxprofit)
        #
        if not prices:
            return 0
        buy = sell = prices[0]
        maxprofit = 0
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                sell = prices[i]
            else:
                sell = max(sell, prices[i])

            maxprofit = max(maxprofit, sell - buy)

        return maxprofit

instance = Solution()
print instance.maxProfit([1, 6])
print instance.maxProfit([2,1,2,1,0,1,2])
print instance.maxProfit([7, 1, 5, 3, 6, 4])
print instance.maxProfit([7, 6, 4, 3, 1])
print instance.maxProfit([3, 4, 5])