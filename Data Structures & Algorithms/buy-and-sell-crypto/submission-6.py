class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        max_zysk = 0

        for price in prices[1:]:

            if price < min_price:
                min_price = price

            else:
                max_zysk = max(max_zysk, price - min_price)

        return max_zysk