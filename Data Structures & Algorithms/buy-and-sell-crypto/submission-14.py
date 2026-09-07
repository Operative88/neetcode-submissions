class Solution:
    def maxProfit(self, prices: List[int]) -> int:    
        # max price musi byc po min price
        # rozważ [1, 2]
        
        max_profit = 0
      
        min_price = prices[0]
       
        max_price = 0

        for index, price in enumerate(prices):
          
            if price < min_price:   
                min_price = price
            
                max_price = max(prices[index:])
           
            max_profit = max(max_profit, max_price - min_price)
        return max_profit