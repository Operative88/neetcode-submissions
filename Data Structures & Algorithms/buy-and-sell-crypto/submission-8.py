class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        max_price = prices[0]
        max_profit = max_price - min_price

        for price in prices:
            if price <= min_price:
                min_price = price
            if price >= max_price:
                max_price = price
            max_profit = max_price - min_price
        
        if max_profit <= 0:
            return 0
        else:
            return max_profit