class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0]

        buy = prices[0] 

        sell = buy
        i = 1
        while i < len(prices):
            if prices[i] < buy :
                buy = prices[i]
                sell = buy
            if prices[i] - buy > profit[-1]:
                sell = prices[i]

            profit.append(sell - buy)
            i += 1


        return max(profit)