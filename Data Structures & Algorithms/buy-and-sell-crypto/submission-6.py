class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j = 0,1
        profit = 0
        res = 0
        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
                j = i + 1
            else:
                profit = prices[j] - prices[i]
                print(profit)
                res = max(profit,res)
                j += 1
        return res