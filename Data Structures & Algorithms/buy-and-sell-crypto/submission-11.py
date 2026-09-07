class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        max_price = prices[-1]
        max_profit = max_price - min_price
        day_buy = 0
        i = 0

        for price in prices:
            if price <= min_price:
                min_price = price
                day_buy = i
            if price >= max_price and i > day_buy:
                max_price = price
            max_profit = max_price - min_price
            i += 1
        
        if max_profit <= 0:
            return 0
        else:
            return max_profit