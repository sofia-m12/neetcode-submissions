class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # thinking two pointer, fast and slow
        max_profit = 0 #return zero if all profits negative
        left = 0

        for right in range(1, len(prices)): #star after left
            if prices[right] < prices[left]:
                left = right #move it up so not negative
            else:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
        return max_profit

