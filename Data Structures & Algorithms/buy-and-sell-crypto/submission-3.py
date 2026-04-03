class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        # Slice the list after the buy index (e.g. i + 1) and find the max sell number
        for i in range(len(prices)):
            buy_price = prices[i]
            sell_start_index = i + 1

            # Edge case: too late to buy/sell
            if sell_start_index >= len(prices):
                return result
            
            # Calculate max profit
            max_sell_price = max(prices[sell_start_index:])
            max_profit = max_sell_price - buy_price
            if max_profit > result:
                result = max_profit

        return result