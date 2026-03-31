class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #profit = sell - buy
        max_profit = 0
        min_buy = float('inf')

        for price in prices:
            min_buy = min(price,min_buy)
            profit = price - min_buy
            max_profit = max(max_profit,profit)
        return max_profit

    
