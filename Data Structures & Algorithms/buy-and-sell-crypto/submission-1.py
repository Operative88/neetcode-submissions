class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
            index = 0
            sort = sorted(prices)

            for a, b in zip(prices, sort):
                
                if a <= b:
                    buy = a
                    index += 1
                    sell = max(prices[index:])
                    profit = sell - buy
                    if profit > 0:
                        return profit
                    else:
                        return 0
                index += 1
