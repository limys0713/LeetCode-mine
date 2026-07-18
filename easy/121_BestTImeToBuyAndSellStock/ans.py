from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                current_profit = price - min_price
                if current_profit > profit:
                    profit = current_profit
            
        return profit