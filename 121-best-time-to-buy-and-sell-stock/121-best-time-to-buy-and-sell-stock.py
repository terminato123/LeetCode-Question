class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         # maximum profit
        max_profit = 0
        
    
        right_max = [0]*len(prices)
        right_max[-1] = prices[-1]
        
        # Create array which stores maximum element to the right of current element.
        for i in range (len(right_max)-2,-1,-1):
            right_max[i] = max(prices[i], right_max[i+1])
    
        
        for i in range (len(prices)-1):
            # calculate maximum profit using right_max array.
            max_profit = max( max_profit,right_max[i+1]-prices[i] )
    
        return max_profit
        