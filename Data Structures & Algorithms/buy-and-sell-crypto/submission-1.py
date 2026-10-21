class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy_idx < sell_idx

        #track max profit
        max_profit = 0

        buy = 0 # want to buy at lowest value

        #loop until buy < sell is false
        for sell in range(1, len(prices)):
            #if there is a lower value, move buy
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                #calculate profit & compare it to max
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)

        return max_profit

        #time: O(n), goting through (n-1) ellemtns in prices
        #space: O(1), no extra storage, just variables!