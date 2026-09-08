class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        max_price = max(prices)

        for index, price in enumerate(prices):
            if price < min_price:
                min_price = price
                max_price = max(prices[index:])
            max_profit = max(max_profit, max_price - min_price)
        return max_profit