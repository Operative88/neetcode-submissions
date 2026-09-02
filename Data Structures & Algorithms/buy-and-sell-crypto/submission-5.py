class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
            min_cena = prices[0]
            max_zysk = 0

            for price in prices[1:]:
                if price < min_cena:
                    min_cena = price
                else:
                    max_zysk = max(max_zysk, price - min_cena)
            
            return max_zysk