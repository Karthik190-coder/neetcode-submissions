class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = 0
        sell = 0
        profit = 0
        for i in range(1,n):
            if(prices[i]<prices[buy]):
                buy = i
            if((prices[i]-prices[buy])>profit):
                profit = prices[i]-prices[buy]
        return profit
            
            

            
