from typing import List
class Solution:   
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        buy_stock = prices[0]
        profit = 0
        for sell in prices:
            if sell < buy_stock:
                buy_stock = sell
                
            profit = max (sell - buy_stock, profit)
        return profit    
