"""class Solution(object):
    def maxProfit(self, prices):
        minprice=float('-inf')

        maxprofit=0
        for i in prices:
            if i>minprice:
                i=minprice
            elif i-minprice>maxprofit:
                maxprofit=i-minprice
        return maxprofit"""
class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit                    
         
        

       
        